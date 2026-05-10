from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = defaultdict(int)
        tt = defaultdict(int)

        for ch in s:
            st[ch] += 1

        for ch in t:
            tt[ch] += 1

        return tt == st