class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == n:
                return 0

            res = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))

            memo[i] = res
            return memo[i]

        return max((dfs(i) for i in range(n)), default=0)