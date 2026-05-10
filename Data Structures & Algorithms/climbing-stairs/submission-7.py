class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [1] * 2

        for i in range(n - 3, -1, -1):
            dp[0], dp[1] = dp[0] + dp[1], dp[0]
        
        return dp[0] + dp[1]

