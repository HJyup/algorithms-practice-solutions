class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        i_1, i_2 = 0, 0
        flip = 0
        while i_1 < len(word1) and i_2 < len(word2):
            if flip == 0:
                res += word1[i_1]
                i_1 += 1
                flip = 1
            else:
                res += word2[i_2]
                i_2 += 1
                flip = 0
            
        if i_1 < len(word1):
            res += word1[i_1:]

        if i_2 < len(word2):
            res += word2[i_2:]

        return res
        