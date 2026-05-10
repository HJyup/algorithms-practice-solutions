from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dt = defaultdict(int)
        t_dt = defaultdict(int)

        for c in s:
            s_dt[c] += 1
        
        for c in t:
            t_dt[c] += 1

        return s_dt == t_dt