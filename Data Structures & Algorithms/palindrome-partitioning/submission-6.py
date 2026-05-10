class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        dp = [[False] * len(s) for _ in range(len(s))]

        palindrome = []
        def backtrack(i: int) -> None:
            if i == len(s):
                res.append(palindrome[:])
                return None

            for j in range(i, len(s)):
                candidate = s[i : j + 1]
                dp[i][j] = candidate == candidate[::-1]

                if dp[i][j]:
                    palindrome.append(candidate)
                    backtrack(j + 1)
                    palindrome.pop()

            return None

        backtrack(0)
        return res