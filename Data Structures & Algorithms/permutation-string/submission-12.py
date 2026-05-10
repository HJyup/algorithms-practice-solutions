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

        if window == perm:
            return True

        for r in range(k, n):
            window[ord(s2[r]) - base] += 1
            window[ord(s2[r - k]) - base] -= 1
            if window == perm:
                return True

        return False
        