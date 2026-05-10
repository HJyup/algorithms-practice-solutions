from collections import defaultdict

class TimeMap:

    def __init__(self):
        # For each key we want to know
        # timestamp ordered array - so we can acces it in order
        # min and max for each key so we can restrict binary search
        # min and max can be derived from the array itself (usign first value and the last)
        # the insertion by timestamp will be always in order
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        stored_values = self.store[key]

        if not stored_values:
            return ''

        left, right = 0, len(stored_values) - 1
        res = ''

        while left <= right:
            mid = (left + right) // 2
            current_timestamp = stored_values[mid][0]
            current_value = stored_values[mid][1]

            if current_timestamp == timestamp:
                return current_value

            elif current_timestamp < timestamp:
                res = current_value
                left = mid + 1

            else:
                right = mid - 1

        return res
