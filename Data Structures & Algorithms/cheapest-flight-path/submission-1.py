import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start, destination, time in flights:
            graph[start].append((destination, time))

        remaining_stops = [-1] * n
        heap = [(0, k, src)]

        while heap:
            time, stops, node = heapq.heappop(heap)
            if node == dst:
                return time

            if stops <= remaining_stops[node]:
                continue

            remaining_stops[node] = stops
            for nei, nei_time in graph[node]:
                heapq.heappush(heap, (time + nei_time, stops - 1, nei))

        return -1