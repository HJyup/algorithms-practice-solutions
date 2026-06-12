class Node:
    def __init__(self, key: int, value: int, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    # Reposnible for only evitction and append (doesn't control the policies inside)    
    # We need shared map between LFU and different LRUs
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.map = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def _evict(self, node: Node) -> Optional[Node]:
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None
        del self.map[node.key]

        return node

    def evictByKey(self, key: int) -> Optional[Node]:
        if key not in self.map:
            return

        return self._evict(self.map[key])

    def evictLast(self) -> Optional[Node]:
        if not self.map:
            return

        return self._evict(self.tail.prev)

    def place(self, node: Node) -> None:
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = self.head
        self.map[node.key] = node

    def isEmpty(self) -> bool:
        return self.head.next is self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.freqs = {} # {freq: LRUCache}
        self.keys = {} # {key: freq}
        self.minFreq = 0 # the last minFrequency we have seen
        
        self.cap = capacity
        self.size = 0

    def _access(self, key: int) -> Optional[Node]:
        if key not in self.keys:
            return

        old_freq = self.keys[key]
        node = self.freqs[old_freq].evictByKey(key)

        if self.freqs[old_freq].isEmpty():
            del self.freqs[old_freq]
            if self.minFreq == old_freq: # Update it so we can always find the min LRU
                self.minFreq += 1

        if not node: 
            return # If we didn't find a key (should not be possible but who knows)

        new_freq = old_freq + 1
        self.keys[key] = new_freq

        if new_freq not in self.freqs:
            self.freqs[new_freq] = LRUCache()

        self.freqs[new_freq].place(node)
        return node

    def _evict(self) -> None:
        if self.minFreq not in self.freqs:
            return

        self.size -= 1
        node = self.freqs[self.minFreq].evictLast()

        del self.keys[node.key]

    def get(self, key: int) -> int:
        node = self._access(key)
        if not node:
            return -1

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self._access(key)
            node.value = value
            return

        if self.size == self.cap:
            self._evict()

        self.minFreq = 1
        if self.minFreq not in self.freqs:
            self.freqs[self.minFreq] = LRUCache()
        self.freqs[self.minFreq].place(Node(key, value))
        self.keys[key] = self.minFreq
        self.size += 1

        return None



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)