class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_n, t_n = len(s), len(t)
        index = lambda x: ord(x) - ord('a')

        if s_n != t_n:
            return False

        s_hash = [0] * 26
        t_hash = [0] * 26

        for i in range(s_n):
            s_hash[index(s[i])] += 1
            t_hash[index(t[i])] += 1

        return s_hash == t_hash