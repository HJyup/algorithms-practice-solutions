class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(subset, idx):
            sm = sum(subset)

            if sm > target:
                return

            if sm == target:
                self.res.append(subset)
                return

            for i in range(idx, len(nums)):
                dfs(subset + [nums[i]], i)

        dfs([], 0)
        return self.res
        

            

        