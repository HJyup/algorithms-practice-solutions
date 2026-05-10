class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()

        idx = -1
        for i, (start, _) in enumerate(intervals):
            if newInterval[0] <= start:
                idx = i
                break

        if idx == -1:
            intervals.append(newInterval)
        
        else:
            intervals.insert(idx, newInterval)

        # Merge
        res = [ intervals[0] ]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])

            else:
                res.append([start, end])

        return res