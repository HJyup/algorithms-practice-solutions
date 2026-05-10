class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        # sort and skip in the current depth
        # i + 1 since "at most once"
        def dfs(comb, idx):
            sm = sum(comb)

            # We can't build more from here therefore it doesnt make sense
            if sm > target:
                return

            # we can accept this comb
            if sm == target:
                res.append(comb)
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(comb + [candidates[i]], i + 1)

        # execute the backtrack
        dfs([], 0)
        return res

        