class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def count(idx):
            if idx >= n:
                return 0

            return cost[idx] + min(count(idx + 1), count(idx + 2))

        return min(count(0), count(1))

        