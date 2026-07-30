import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        queue = [(capital[i], profits[i]) for i in range(len(profits))]
        queue.sort()

        ans = w

        heap = []
        i = 0

        while k > 0:
            while i < len(queue) and queue[i][0] <= ans:
                heapq.heappush(heap, -queue[i][1])
                i += 1

            if not heap:
                break

            cap = heapq.heappop(heap)
            ans += (-cap)
            k -= 1

        return ans
