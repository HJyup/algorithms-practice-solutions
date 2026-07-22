class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        curr = []
        def dfs(sm: int, i: int):
            if sm == target:
                res.append(curr[:])
                return

            if sm > target:
                return

            for j in range(i, len(candidates)):
                if i == j or candidates[j] != candidates[j - 1]:
                    curr.append(candidates[j])
                    dfs(sm + candidates[j], j + 1)
                    curr.pop()

        dfs(0, 0)
        return res