class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n, res = len(candidates), []

        path = []
        def dfs(start, sm):
            if sm == target:
                res.append(path[:])

            if sm >= target and start == n:
                return None

            for i in range(start, n):
                if candidates[i] > target:
                    break

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, sm + candidates[i])
                path.pop()

            return None

        dfs(0, 0)
        return res