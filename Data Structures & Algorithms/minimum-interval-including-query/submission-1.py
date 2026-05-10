import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(query, idx) for idx, query in enumerate(queries)]
        queries.sort()

        intervals.sort()
        min_intervals = [-1 for _ in range(len(queries))]

        idx, heap = 0, []
        for query, i in queries:
            while heap and not (intervals[heap[0][1]][0] <= query <= intervals[heap[0][1]][1]):
                heapq.heappop(heap)

            while idx < len(intervals):
                if (intervals[idx][0] <= query <= intervals[idx][1]):
                    heapq.heappush(heap, (intervals[idx][1] - intervals[idx][0] + 1, idx))

                if query < intervals[idx][0]:
                    break
                    
                idx += 1

            if heap:
                min_intervals[i] = heap[0][0]

        return min_intervals