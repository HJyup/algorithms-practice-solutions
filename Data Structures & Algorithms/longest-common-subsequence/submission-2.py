class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            row = [0] * (m + 1)

            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    row[j] = 1 + dp[j + 1]

                else:
                    row[j] = max(dp[j], row[j + 1])

            dp = row

        return dp[0]