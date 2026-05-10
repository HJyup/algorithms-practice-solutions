class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if k > n:
            return False

        base = ord('a')
        perm = [0] * 26
        window = [0] * 26

        for ch in s1:
            perm[ord(ch) - base] += 1

        for ch in s2[:k]:
            window[ord(ch) - base] += 1

        matches = sum(1 for i in range(26) if perm[i] == window[i])
        if matches == 26:
            return True

        for r in range(k, n):
            add = ord(s2[r]) - base
            drop = ord(s2[r - k]) - base

            window[add] += 1
            if window[add] == perm[add]:
                matches += 1
            elif window[add] - 1 == perm[add]:
                matches -= 1

            window[drop] -= 1
            if window[drop] == perm[drop]:
                matches += 1
            elif window[drop] + 1 == perm[drop]:
                matches -= 1

            if matches == 26:
                return True

        return False
        