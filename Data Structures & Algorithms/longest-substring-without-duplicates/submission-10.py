class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            max_len = max(max_len, r - l + 1)

        return max_len