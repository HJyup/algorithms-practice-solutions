class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = {}
        
        def dfs(i: int, j: int) -> int:
            state = (i, j)

            if state in memo:
                return memo[state]
            
            if i >= n or j >= m:
                return 0

            if text1[i] == text2[j]:
                memo[state] = 1 + dfs(i + 1, j + 1)
                return memo[state]

            memo[state] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[state]

        return dfs(0, 0)