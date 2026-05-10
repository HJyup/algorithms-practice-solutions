class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(i, curr, sm):
            if sm == target:
                res.append(curr[:])
                return None

            if i == n or sm > target:
                return None

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                curr.append(candidates[j])
                dfs(j + 1, curr, sm + candidates[j])
                curr.pop()

            return None

        dfs(0, [], 0)
        return res