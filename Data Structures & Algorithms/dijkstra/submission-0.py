from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)
        for s, e, w in edges:
            graph[s].append((e, w))

        res = {}
        heap = [(0, src)]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in res:
                continue

            res[n1] = w1
            for n2, w2 in graph[n1]:
                heapq.heappush(heap, (w2 + w1, n2))

        for i in range(n):
            if i not in res:
                res[i] = -1

        return res