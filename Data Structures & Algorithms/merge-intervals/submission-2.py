class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        start, end = intervals[0]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start <= end:
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end

        res.append([start, end])

        return res