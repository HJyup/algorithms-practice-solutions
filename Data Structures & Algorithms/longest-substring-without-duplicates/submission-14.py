class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()

        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.discard(s[left])
                left += 1

            res = max(right - left + 1, res)
            window.add(s[right])

        return res