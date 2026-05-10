import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            x, y = -x, -y

            diff = x - y
            if diff:
                heapq.heappush(heap, -diff)

        return -heap[0] if len(heap) > 0 else 0