from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = -1

        graph = defaultdict(list)
        for s, e, time in times:
            graph[s].append((e, time))

        path = {}
        heap = [(0, k)]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in path:
                continue

            path[n1] = w1
            res = max(res, w1)

            for n2, w2 in graph[n1]:
                heapq.heappush(heap, (w1 + w2, n2))

        for i in range(1, n + 1):
            if i not in path:
                return -1

        return res