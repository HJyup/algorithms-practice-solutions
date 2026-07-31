class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], x[1]))

        for i, interval in enumerate(intervals):
            start, _ = interval
            if newInterval[0] <= start:
                intervals.insert(i, newInterval)
                break

        if len(intervals) == n:
            intervals.append(newInterval)

        ans = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])

        return ans