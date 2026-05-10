from collections import defaultdict

# Space O(m * n)
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    # O(1) - instant lol
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        
    # O(log(n)) - binary search
    def get(self, key: str, timestamp: int) -> str:
        pairs = self.data[key]
        l, r = 0, len(pairs) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if pairs[mid][0] == timestamp:
                return pairs[mid][1]

            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res  
