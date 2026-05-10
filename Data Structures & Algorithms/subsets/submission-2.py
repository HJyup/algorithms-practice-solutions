class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(subset, count):
            if count == len(nums):
                self.res.append(subset)
                return

            dfs(subset, count + 1)
            dfs(subset + [nums[count]], count + 1)
        
        dfs([], 0)
        return self.res
        

            





        