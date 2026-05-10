class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert into position where it has to overlap or be okay with it
        # [1, 3], [2, 5], [4, 6]

        idx = -1
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                idx = i
                break

        if idx == -1:
            intervals.append(newInterval)
        
        else:
            intervals.insert(idx, newInterval)

        # merge
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], end)
            else:
                res.append([start, end])

        return res