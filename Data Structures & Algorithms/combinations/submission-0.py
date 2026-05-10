class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combinations = letters canno be the same
        # n - integers
        res = []

        path = []
        def dfs(start: int, to_add: int) -> None:
            if to_add == 0:
                res.append(path[:])
                return None

            if to_add > (n + 1 - start):
                return None

            for num in range(start, n + 1):
                path.append(num)
                dfs(num + 1, to_add - 1)
                path.pop()

            return None

        dfs(1, k)
        return res