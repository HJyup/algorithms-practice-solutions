class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        def dfs(sm: int, i: int):
            if sm == target:
                res.append(curr[:])
                return None

            if i >= len(nums) or sm > target:
                return None

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(sm + nums[j], j)
                curr.pop()

            return None

        dfs(0, 0)
        return res