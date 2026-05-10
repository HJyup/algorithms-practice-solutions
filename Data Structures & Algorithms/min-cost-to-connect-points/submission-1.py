import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()

        heap = [(0, tuple(points[0]))]
        res = 0

        while heap:
            dst, point = heapq.heappop(heap)
            if point in visited:
                continue

            visited.add(point)
            res += dst

            for nei_point in points:
                nei_point = tuple(nei_point)
                
                if nei_point in visited:
                    continue

                nei_dst = abs(point[0] - nei_point[0]) + abs(point[1] - nei_point[1])
                heapq.heappush(heap, (nei_dst, nei_point))

        return res