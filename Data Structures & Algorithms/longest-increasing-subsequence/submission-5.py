class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(start: int, prev: int) -> int:
            state = (start, prev)

            if state in memo:
                return memo[state]

            if start == n:
                return 0

            res = 0
            for i in range(start, n):
                if prev == None or nums[i] > prev:
                    res = max(res, 1 + dfs(i + 1, nums[i]))

            memo[state] = res
            return memo[state]

        return dfs(0, None)