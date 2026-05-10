class Solution:
    def rob(self, nums: List[int]) -> int:
        # we have two choices: either we take this house skipping next or we skip this to take the next
        n = len(nums)
        dp = [nums[n - 1], 0]

        for i in range(n - 2, -1, -1):
            dp[0], dp[1] = max(nums[i] + dp[1], dp[0]), dp[0]
        
        return max(dp[0], dp[1])