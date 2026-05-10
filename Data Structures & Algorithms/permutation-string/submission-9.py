class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = [0] * 26
        window = [0] * 26
        k = len(s1)

        for ch in s1:
            count[ord(ch) - ord('a')] += 1

        for ch in s2[:k]:
            window[ord(ch) - ord('a')] += 1

        if window == count:
            return True

        for r in range(k, len(s2)):
            left_index = ord(s2[r - k]) - ord('a')
            right_index = ord(s2[r]) - ord('a')

            window[left_index] -= 1
            window[right_index] += 1

            if window == count:
                return True

        return False