class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        path = []
        def dfs(start):
            nonlocal res

            if start == n:
                res.append(path[:])
                return None

            for end in range(start, n):
                substring = s[start : end + 1]

                if substring == substring[::-1]:
                    path.append(substring)
                    dfs(end + 1)
                    path.pop()

            return None
            
        dfs(0)
        return res
        