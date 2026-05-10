from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = defaultdict(int)

        for ch in s1:
            perm[ch] += 1

        k = len(s1) - 1
        for l in range(0, len(s2)):
            check = defaultdict(int)
            r = min(len(s2) - 1, l + k)

            for ch in s2[l : r + 1]:
                check[ch] += 1

            if check == perm:
                return True

        return False