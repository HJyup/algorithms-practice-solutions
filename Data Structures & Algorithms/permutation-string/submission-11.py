class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count, window = [0] * 26, [0] * 26
        k = len(s1)

        for i in range(0, len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if window == count:
            return True

        for r in range(k, len(s2)):
            window[ord(s2[r - k]) - ord('a')] -= 1
            window[ord(s2[r]) - ord('a')] += 1

            if window == count:
                return True

        return False