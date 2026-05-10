class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True

        i = 0

        for letter in t:
            if letter == s[i]:
                i += 1

            if i == len(s):
                return True

        return False
        