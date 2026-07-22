class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        curr = []
        def dfs(num: int):
            if len(curr) == k:
                res.append(curr[:])
                return None

            if num == n + 1:
                return None

            # take this num
            curr.append(num)
            dfs(num + 1)
            curr.pop()

            # skip this num
            dfs(num + 1)

            return None

        dfs(1)
        return res