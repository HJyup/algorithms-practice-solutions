from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        window = defaultdict(int)
        k = len(s1)

        for ch in s1:
            count[ch] += 1

        for ch in s2[0: k]:
            window[ch] += 1

        if window == count:
            return True

        l = 0
        for r in range(k, len(s2)):
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            l += 1
            window[s2[r]] += 1

            if window == count:
                return True
            

        return False