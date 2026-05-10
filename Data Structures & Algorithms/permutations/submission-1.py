class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.res = []

        def dfs(perm):
            if len(perm) == len(nums):
                self.res.append(perm)
                return

            for i in range(len(nums)):
                if not self.used[i]:
                    self.used[i] = True
                    dfs(perm + [nums[i]])
                    self.used[i] = False

        dfs([])
        return self.res
        
        