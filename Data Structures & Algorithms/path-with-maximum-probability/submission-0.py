from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            s, e = edges[i][0], edges[i][1]
            graph[s].append((e, succProb[i]))
            graph[e].append((s, succProb[i]))

        score = {}
        heap = [(-1.0, start_node)]
        while heap:
            w1, n1 = heapq.heappop(heap)
            w1 = -w1

            if n1 in score:
                continue

            score[n1] = w1
            if n1 == end_node:
                break

            for n2, w2 in graph[n1]:
                heapq.heappush(heap, (-(w2 * w1), n2))
        
        if end_node in score:
            return score[end_node]

        return 0.0
        