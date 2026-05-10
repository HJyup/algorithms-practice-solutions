class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # because we either just to last element paying the price or jsut directly to the end
        dp = [cost[n - 1], 0]

        for i in range(n - 2, -1, -1):
            dp[0], dp[1] = cost[i] + min(dp[0], dp[1]), dp[0]

        return min(dp[0], dp[1])