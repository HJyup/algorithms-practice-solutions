class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        n = len(s)

        window, left = set(), 0
        for right in range(n):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            longest = max(longest, right - left + 1)

        return longest