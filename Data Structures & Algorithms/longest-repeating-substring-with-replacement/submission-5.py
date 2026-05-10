from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l, res = 0, 0

        for r in range(len(s)):
            window[s[r]] += 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res