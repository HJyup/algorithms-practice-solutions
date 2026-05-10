class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]):
            return math.sqrt(point[0]**2 + point[1]**2)

        heap = [(-distance(point), point) for point in points]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return [item[1] for item in heap]
        
