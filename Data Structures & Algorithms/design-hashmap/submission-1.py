class MyHashMap:

    def __init__(self):
        self.capacity = 16
        self.count = 0
        self.PROBE_STEP = 7
        self.LOAD_FACTOR = 0.7

        # None - empty
        self.arr = [None] * self.capacity
        # hashed key to store when we can keep probing
        self.tombstones = set()


    def _hash(self, key, idx):
        fst = key % self.capacity
        snd = 1 + (key % (self.capacity - 1))

        return (fst + idx * snd) % self.capacity

    def resize(self):
        self.capacity *= 2
        self.tombstones = set()

        prev_arr = self.arr.copy()
        self.arr = [None] * self.capacity

        for item in prev_arr:
            if item is None:
                continue

            self.put(item[0], item[1])


    def put(self, key: int, value: int) -> None:
        curr = 0
        self.count += 1

        if self.count / self.capacity > self.LOAD_FACTOR:
            self.resize()

        while curr < self.capacity:
            hashed = self._hash(key, curr)

            if self.arr[hashed] is None:
                self.arr[hashed] = (key, value)
                self.tombstones.discard(hashed)

                return None

            if self.arr[hashed][0] == key:
                self.arr[hashed] = (key, value)
                
                return None

            curr += 1

    def get(self, key: int) -> int:
        curr = 0

        while curr < self.capacity:
            hashed = self._hash(key, curr)
            
            # To continue do probbing
            if self.arr[hashed] is None and hashed not in self.tombstones:
                return -1

            if self.arr[hashed] is not None and self.arr[hashed][0] == key:
                return self.arr[hashed][1]

            curr += 1

        return -1

    def remove(self, key: int) -> None:
        curr = 0

        while curr < self.capacity:
            hashed = self._hash(key, curr)

            if self.arr[hashed] is None and hashed not in self.tombstones:
                return None

            if self.arr[hashed] is not None and self.arr[hashed][0] == key:
                self.arr[hashed] = None
                self.tombstones.add(hashed)

                return None

            curr += 1

        return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)