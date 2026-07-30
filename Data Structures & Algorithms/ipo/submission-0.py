import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        queue = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(queue)
        
        ans = w

        heap = []
        while k > 0:
            while queue and queue[0][0] <= ans:
                _, val = heapq.heappop(queue)
                heapq.heappush(heap, -val)

            if not heap:
                break

            cap = heapq.heappop(heap)
            ans += (-cap)
            k -= 1

        return ans
