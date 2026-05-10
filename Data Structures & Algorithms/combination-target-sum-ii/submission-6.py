class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        n = len(candidates)
        res = []

        path = []
        def backtrack(i: int, sm: int) -> None:
            if sm == target:
                res.append(path[:])
                return None

            if i == n or sm > target:
                return None

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                backtrack(j + 1, sm + candidates[j])
                path.pop()

            return None

        backtrack(0, 0)
        return res