class Node:
    def __init__(self, key: int, value: int, prev = None, next = None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0

        # Linked List implementation
        self.head = None
        self.tail = None

    def place(self, node: Node):
        # If no elements in the list
        if not self.head:
            self.head = node
            self.tail = node

        # If head exists
        else:
            node.next = self.head
            self.head.prev = node

            self.head = node

        return None

    def evict(self):
        # Eviction is just extraction of last element
        evicted = self.extract(self.tail)
        
        del self.cache[evicted.key]
        self.size -= 1
        return None

    def extract(self, node: Node):
        if not node:
            return None 

        # Head == Tail
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        # Only head
        elif node == self.head:
            self.head.next.prev = None
            self.head = self.head.next
        
        # Only tail
        elif node == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        
        node.next = None
        node.prev = None
        return node

    def promote(self, node: Node):
        node = self.extract(node)
        self.place(node)

        return None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.promote(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        # Key not exist
        # 1. Place the node at the head
        # 2. Update cache
        # 3. If capacity is reached, then we need to evict from the tail.

        # Key exists
        # 1. Take the key from the priority list
        # 2. Remove it from the priority list
        # 3. Place it at the top
        if key not in self.cache:
            if self.size == self.capacity:
                self.evict()

            node = Node(key, value)
            self.size += 1

            self.cache[key] = node
            self.place(node)

        else:
            node = self.cache[key]
            node.value = value

            self.promote(node)

        return None
        
