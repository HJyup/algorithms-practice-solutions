class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        seen, curr = set(), []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            chosen = set()
            for i in range(len(nums)):
                if i not in seen and nums[i] not in chosen:
                    seen.add(i)
                    curr.append(nums[i])
                    chosen.add(nums[i])
                    dfs()
                    curr.pop()
                    seen.remove(i)

        dfs()
        return res