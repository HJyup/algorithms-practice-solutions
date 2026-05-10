class Solution:
    def longestPalindrome(self, s: str) -> str:
        # We have 2 possible solutions here. or we start from this value and we cna do odd palindrome
        # or we can do even plindrome
        n = len(s)
        mx = 0
        res = ''

        def getPalindromeIndices(left: int, right: int) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(n):
            l1, r1 = getPalindromeIndices(i, i)
            if (r1 - l1 + 1) > len(res):
                res = s[l1 : r1 + 1]

            l2, r2 = getPalindromeIndices(i, i + 1)
            if (r2 - l2 + 1) > len(res):
                res = s[l2 : r2 + 1]

        return res