from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]
        
        print(vals, key, timestamp)
        if len(vals) == 0:
            return ""

        left, right = 0, len(vals) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] < timestamp:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return vals[ans][1] if ans != -1 else ""
