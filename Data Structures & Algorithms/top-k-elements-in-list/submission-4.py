from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num in freq:
            if len(heap) >= k:
                heapq.heappushpop(heap, (freq[num], num))
            else:
                heapq.heappush(heap, (freq[num], num))

        return [num for _, num in heap]