from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wnd = defaultdict(int)
        ans = 0

        l = 0
        freq = 0
        for r in range(len(s)):
            wnd[s[r]] += 1
            freq = max(freq, wnd[s[r]])

            if (r - l + 1) - freq > k:
                wnd[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans