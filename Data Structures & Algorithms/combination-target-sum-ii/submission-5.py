from collections import deque

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n, res = len(candidates), []

        q = deque([(0, [], 0)])

        while q:
            start, path, sm = q.popleft()

            if sm == target:
                res.append(path)

            if sm >= target or start == n or candidates[start] > target:
                continue

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                q.append((i + 1, path + [candidates[i]], sm + candidates[i]))

        return res

            