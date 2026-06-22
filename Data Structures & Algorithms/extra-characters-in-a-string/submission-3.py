class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        memo = {}

        def dfs(i: int):
            if i in memo:
                return memo[i]

            if i == n:
                return 0

            ans = 1 + dfs(i + 1)
            for j in range(i, n):
                if s[i: j + 1] in words:
                    ans = min(ans, dfs(j + 1))

            memo[i] = ans
            return memo[i]

        return dfs(0)
