class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length, t_length = len(s), len(t)

        if s_length > t_length:
            return False

        if s_length == 0:
            return True

        idx = 0
        for i in range(t_length):
            if s[idx] == t[i]:
                idx += 1

            if idx == s_length:
                return True

        return idx == s_length

