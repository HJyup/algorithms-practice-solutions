class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        candidate = strs[0]

        for word in strs:
            if len(word) < len(candidate):
                candidate = word

        prefix = ''

        for i in range(len(candidate)):
            for j in range(len(strs)):
                if candidate[i] != strs[j][i]:
                    return prefix

            prefix += candidate[i]

        return prefix