class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr, seen = [], set()
        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
                return None

            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    curr.append(nums[i]) # works because of unique elements
                    dfs()
                    curr.pop()
                    seen.remove(nums[i])
                
            return None

        dfs()
        return res