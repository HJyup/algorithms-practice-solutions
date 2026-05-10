class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            val = heapq.heappop(heap) - heapq.heappop(heap)
            if val != 0:
                heapq.heappush(heap, val)
            
        heap.append(0)
        return abs(heap[0])
    