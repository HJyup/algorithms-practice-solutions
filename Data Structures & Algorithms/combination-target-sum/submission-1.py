class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, sm, start):
            if sm > target:
                return
            if sm == target:
                res.append(subset)
                return

            for i in range(start, len(nums)):
                dfs(subset + [nums[i]], sm + nums[i], i)

        dfs([], 0, 0)
        return res
        

            

        