class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i, point in enumerate(points):
            dst = -1 * (pow(point[0], 2) + pow(point[1], 2))

            if len(heap) == k:
                if dst > heap[0][0]:
                    heapq.heappushpop(heap, (dst, i))
            else:
                heapq.heappush(heap, (dst, i))

        return [points[i] for _, i in heap]