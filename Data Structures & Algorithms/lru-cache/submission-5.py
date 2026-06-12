class Node:
    def __init__(self, key: int, value: int, next=None, prev=None):
        self.key = key # for correct eviciton
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        # metadata
        self.capacity = capacity
        self.size = 0

        # dummy nodes
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        # connections
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.key_map = {} # key -> ListNode

    def _place(self, node: Node) -> None:
        self.size += 1

        nxt = self.head.next # new next for a new node
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

        self.key_map[node.key] = node

    def _evict(self, node: Node) -> Node:
        self.size -= 1

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

        del self.key_map[node.key]
        return node

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        node = self._evict(node)
        self._place(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            self.key_map[key].value = value
            node = self._evict(self.key_map[key])
            self._place(node)
            return

        if self.size == self.capacity:
            evicted = self._evict(self.tail.prev)
        
        node = Node(key, value)
        self._place(node)
