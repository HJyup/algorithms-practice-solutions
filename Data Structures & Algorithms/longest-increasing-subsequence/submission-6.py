class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(i: int) -> int:
            if i == n:
                return 0

            res = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))

            return res

        return max((dfs(i) for i in range(n)), default=0)