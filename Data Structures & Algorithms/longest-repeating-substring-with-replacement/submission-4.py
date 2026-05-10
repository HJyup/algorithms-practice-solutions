class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        window = {}
        l, res = 0, 0
        if len(chars) == 1:
            return len(s)

        for c in chars:
            window[c] = 0

        for r in range(len(s)):
            window[s[r]] += 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res