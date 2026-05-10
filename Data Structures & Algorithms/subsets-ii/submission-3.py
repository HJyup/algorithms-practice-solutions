class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []

        path = []
        def dfs(i):
            nonlocal res

            if i == n:
                res.append(path[:])
                return None

            # Insert
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            # Skip
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

            return None
        
        dfs(0)
        return res