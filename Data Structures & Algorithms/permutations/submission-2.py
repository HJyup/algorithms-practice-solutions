class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        candidate, used = [], set()
        def dfs():
            nonlocal res

            if len(used) == n:
                res.append(candidate[:])
                return None

            for i in range(n):
                if nums[i] not in used:
                    candidate.append(nums[i]), used.add(nums[i])
                    dfs()
                    candidate.pop(), used.remove(nums[i])

            return None

        dfs()
        return res