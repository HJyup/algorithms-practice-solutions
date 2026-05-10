class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        self.res = []

        def dfs(subset, idx):
            self.res.append(subset)

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                
                dfs(subset + [nums[i]], i + 1)

        dfs([], 0)
        return self.res
        
        