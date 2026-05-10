class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def count(idx):
            if idx >= n:
                return 0

            if idx in memo:
                return memo[idx]

            memo[idx] = cost[idx] + min(count(idx + 1), count(idx + 2))
            return memo[idx]

        return min(count(0), count(1))

        