import heapq
from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        visited = set()
        dst = 0

        heap = [(0, k)]
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            dst = max(dst, weight)

            for nei, nei_weight in graph[node]:
                heapq.heappush(heap, (weight + nei_weight, nei))

        return dst if len(visited) == n else -1