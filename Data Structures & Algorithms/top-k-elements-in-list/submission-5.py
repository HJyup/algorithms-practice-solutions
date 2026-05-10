from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))

        return [num for _, num in heap]