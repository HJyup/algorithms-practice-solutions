class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None:
        new_tail = Node(value)
        if not self.head:  # If the deque is empty
            self.head = new_tail
            self.tail = new_tail
        else:  # If the deque is not empty
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail

    def appendleft(self, value: int) -> None:
        new_head = Node(value)
        if not self.head:  # If the deque is empty
            self.head = new_head
            self.tail = new_head
        else:  # If the deque is not empty
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    def pop(self) -> int:
        if not self.tail:  # If deque is empty
            return -1
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:  # If there is still an element left
            self.tail.next = None
        else:  # If deque is now empty
            self.head = None
        return temp.value

    def popleft(self) -> int:
        if not self.head:  # If deque is empty
            return -1
        temp = self.head
        self.head = self.head.next
        if self.head:  # If there is still an element left
            self.head.prev = None
        else:  # If deque is now empty
            self.tail = None
        return temp.value
