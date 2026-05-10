class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # When we are dealing wuth subsets we need to ask a qesion
        # Do we want to include this number or not?
        n = len(nums)
        path, res = [], []

        def dfs(i):
            if i >= n:
                res.append(path[:])
                return None
            
            # Include the value
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            # Do not include the value
            dfs(i + 1)

            return None

        dfs(0)
        return res