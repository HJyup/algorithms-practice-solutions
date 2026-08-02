import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(i, q) for i, q in enumerate(queries)]
        queries.sort(key=lambda x: x[1])

        ans = [-1] * len(queries)

        queue = [i for i in range(len(intervals))]
        queue.sort(key=lambda x: intervals[x][0])

        queue.reverse() # it's like stack but it will be used as a queue

        # the problem, we have 2 things to sort about, correct maintaince of possible intervals
        # then from this intervals we need to chose with the lest diff

        # so heap should contain diff, but the maintaing for possible heaps should be correct

        heap = []
        for q_idx, q in queries:
            while queue and q >= intervals[queue[-1]][0]: # so start of them is bigger than q
                idx = queue.pop()
                heapq.heappush(heap, (intervals[idx][1] - intervals[idx][0] + 1, idx))

            while heap and intervals[heap[0][1]][1] < q:
                heapq.heappop(heap) # remove intetvals which are now stale

            if heap:
                ans[q_idx] = heap[0][0]

        return ans