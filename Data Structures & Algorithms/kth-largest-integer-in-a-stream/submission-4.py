import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.capacity = k

        for num in nums:
            if len(self.heap) == self.capacity:
                if num > self.heap[0]:
                    heapq.heappushpop(self.heap, num)
            else:
                heapq.heappush(self.heap, num)

        return None

    def add(self, val: int) -> int:
        if len(self.heap) == self.capacity:
                if val > self.heap[0]:
                    val = heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0]
        
        
