class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n, res = len(candidates), []

        path = []
        def dfs(i, curr):
            nonlocal res

            if curr == target:
               res.append(path[:]) 

            if curr >= target or i == n:
                return None

            
            path.append(candidates[i])
            dfs(i + 1, curr + candidates[i])
            path.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, curr)

            return None

        dfs(0, 0)
        return res