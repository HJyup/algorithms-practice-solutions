class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1

        if n < 0:
            return 0

        memo = [1, 1]
        for i in range(2, n + 1):
            memo[0], memo[1] = memo[1], memo[0] + memo[1]

        return memo[1]
        