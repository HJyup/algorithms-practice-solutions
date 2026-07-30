class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 0, 1

        for _ in range(n):
            dp1, dp2 = dp2, dp1 + dp2

        return dp2