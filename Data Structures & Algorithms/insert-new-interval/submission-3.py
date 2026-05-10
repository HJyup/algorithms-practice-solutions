class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1. Insert to make merge possible
        is_inserted = False
        for i, interval in enumerate(intervals):
            start = interval[0]

            if start >= newInterval[0]:
                is_inserted = True
                intervals.insert(i, newInterval)
                break

        if not is_inserted:
            intervals.append(newInterval)

        # 2. Merge intervals
        res = []
        
        for start, end in intervals:
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)

            else:
                res.append([start, end])

        return res
        