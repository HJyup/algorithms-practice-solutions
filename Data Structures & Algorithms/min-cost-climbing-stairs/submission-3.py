class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dfs(start: int) -> int:
            if start in memo:
                return memo[start]

            if start >= n:
                return 0

            memo[start] = cost[start] + min(dfs(start + 1), dfs(start + 2))
            return memo[start]

        return min(dfs(0), dfs(1))