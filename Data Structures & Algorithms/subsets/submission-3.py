class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.subset = []

        def dfs(idx):
            if idx == len(nums):
                self.res.append(self.subset[:])
                return

            self.subset.append(nums[idx])
            dfs(idx + 1)
            self.subset.pop()


            dfs(idx + 1)


        dfs(0)
        return self.res

            





        