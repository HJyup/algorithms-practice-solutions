class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dst = [float('inf')] * n
        heap = [(0, k)]
        while heap:
            node_weight, node = heapq.heappop(heap)
            if dst[node - 1] != float('inf'):
                continue

            dst[node - 1] = node_weight
            for nei, nei_weight in graph[node]:
                heapq.heappush(heap, (node_weight + nei_weight, nei))

        mx = 0
        for weight in dst:
            if weight == float('inf'):
                return -1

            mx = max(mx, weight)

        return mx