import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-value for value in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            rem = math.isqrt(-heapq.heappop(heap))
            heapq.heappush(heap, -rem)

        return -sum(heap)