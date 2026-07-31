class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0

        prev = None
        for start, end in intervals:
            if prev is not None and start < prev:
                ans += 1
                prev = min(end, prev)
            else:
                prev = end

        return ans