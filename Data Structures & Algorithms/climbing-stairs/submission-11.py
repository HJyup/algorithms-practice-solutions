class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == n:
                return 1

            if i > n:
                return 0

            memo[i] = dfs(i + 2) + dfs(i + 1)
            return memo[i]

        return dfs(0)
        