class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
            
        # dp[0] represents ways to reach current step
        # dp[1] represents ways to reach the previous step
        dp = [1, 1]

        for num in range(n - 1):
            # The new 'current' is the sum of the two previous states
            # We shift the old 'current' into 'previous'
            dp[0], dp[1] = dp[0] + dp[1], dp[0]
        
        return dp[0]
        