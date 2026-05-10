class HashPair:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def hash(self, key: int) -> int:
        return key % self.capacity


    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        curr = self.arr[hash_key]

        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next

        new_pair = HashPair(key, value, self.arr[hash_key])
        self.arr[hash_key] = new_pair
        self.size += 1

        if self.size * 2 >= self.capacity:
            self.resize()
        

    def get(self, key: int) -> int:
        hash_key = self.hash(key)

        curr = self.arr[hash_key]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1


    def remove(self, key: int) -> bool:
        hash_key = self.hash(key)
        curr = self.arr[hash_key]

        if curr and curr.key == key:
            self.arr[hash_key] = curr.next  # Remove the head
            self.size -= 1
            return True

        prev = None
        while curr:
            if curr.key == key:
                prev.next = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next

        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        old_arr = self.arr
        self.capacity *= 2
        self.arr = [None] * self.capacity
        self.size = 0

        for head in old_arr:
            curr = head
            while curr:
                self.insert(curr.key, curr.val)
                curr = curr.next

