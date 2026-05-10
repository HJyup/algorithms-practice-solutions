class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        candidate = min(strs, key=len)

        prefix = ''
        for i in range(len(candidate)):
            for j in range(len(strs)):
                if candidate[i] != strs[j][i]:
                    return prefix

            prefix += candidate[i]

        return prefix