class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev = float('-inf')
        to_remove = 0 

        for start, end in intervals:
            if start < prev:
                to_remove += 1
                prev = min(prev, end)
            else:
                prev = end

        return to_remove