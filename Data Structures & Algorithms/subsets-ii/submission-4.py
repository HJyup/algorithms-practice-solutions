class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        curr = []
        def dfs(i: int):
            res.append(curr[:])

            for j in range(i, len(nums)):
                if i == j or nums[j] != nums[j - 1]:
                    curr.append(nums[j])
                    dfs(j + 1)
                    curr.pop()

            return None

        dfs(0)
        return res