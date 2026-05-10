class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(start: int, previous: Optional[int]) -> int:
            if (start, previous) in memo:
                return memo[(start, previous)]

            if start == n:
                return 0

            res = 0
            for i in range(start, n):
                if previous == None or nums[i] > previous:
                    res = max(res, 1 + dfs(i + 1, nums[i]))

            memo[(start, previous)] = res
            return memo[(start, previous)]

        return dfs(0, None)
        