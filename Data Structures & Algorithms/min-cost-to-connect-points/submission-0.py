import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()

        heap = [(0, points[0])]
        res = 0

        while heap:
            dst, point = heapq.heappop(heap)
            point = tuple(point)

            if point in visited:
                continue

            visited.add(point)
            res += dst

            for nei_point in points:
                if tuple(nei_point) in visited:
                    continue

                nei_dst = abs(point[0] - nei_point[0]) + abs(point[1] - nei_point[1])
                heapq.heappush(heap, (nei_dst, nei_point))

        return res