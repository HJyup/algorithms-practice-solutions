class Node:
    def __init__(self, val: int, next=None, prev=None):
        self.value = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head 
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # Store previous value
        prev = self.tail.prev

        # Create new value
        val = Node(value)
        self.size += 1

        # Connect it
        prev.next = val
        val.prev = prev
        val.next = self.tail
        self.tail.prev = val

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1

        return True

    def Front(self) -> int:
        return self.head.next.value if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.tail.prev.value if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()