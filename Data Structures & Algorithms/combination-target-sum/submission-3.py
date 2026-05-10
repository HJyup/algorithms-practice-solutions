class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        path = []
        def dfs(i, sm):
            nonlocal res

            if sm == target:
                res.append(path[:])
                return None

            if i >= n or sm > target:
                return None

            for i in range(i, n):
                path.append(nums[i])
                dfs(i, sm + nums[i])
                path.pop()

            return None

        dfs(0, 0)
        return res