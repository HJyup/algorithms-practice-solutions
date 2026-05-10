from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = defaultdict(int)
        check = defaultdict(int)
        k = len(s1)

        for ch in s1:
            perm[ch] += 1

        for ch in s2[0: k]:
            check[ch] += 1

        if check == perm:
            return True

        l = 0
        for r in range(k, len(s2)):
            check[s2[l]] -= 1
            if check[s2[l]] <= 0:
                del check[s2[l]]

            l += 1
            check[s2[r]] += 1

            if check == perm:
                return True
            

        return False