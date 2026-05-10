class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, k)]
        used = [0] * n

        while heap:
            weight, node, stops = heapq.heappop(heap)       
            if node == dst:
                return weight

            if used[node] != 0 and stops <= used[node] or stops == -1:
                continue

            used[node] = stops
            for nei, nei_weight in graph[node]:
                heapq.heappush(heap, (weight + nei_weight, nei, stops - 1))
       
        return -1