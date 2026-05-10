class Solution:
    def rob(self, nums: List[int]) -> int:
        # we have two choices: either we take this house skipping next or we skip this to take the next
        n = len(nums)
        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            if i >= n:
                return 0

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        return dfs(0)
        