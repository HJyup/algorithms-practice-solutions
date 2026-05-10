class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        length = 0

        def check_bounds(left, right):
            return left >= 0 and right < len(s)

        for i in range(len(s)):
            l, r = i, i
            while check_bounds(l, r) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > length:
                    idx = l
                    length = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while check_bounds(l, r) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > length:
                    idx = l
                    length = r - l + 1
                l -= 1
                r += 1 

        return s[idx: idx + length]