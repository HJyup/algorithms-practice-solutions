from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        
        min_heap = [] 

        for num, freq in frequency_map.items():
            heapq.heappush(min_heap, (freq, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            result.append(num)
        
        return result
                    

        


        

        