class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []

        def dfs(comb, idx):
            sm = sum(comb)

            if sm > target:
                return

            if sm == target:
                self.res.append(comb)
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                dfs(comb + [candidates[i]], i + 1)

        dfs([], 0)
        return self.res

        