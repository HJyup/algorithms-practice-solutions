class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        i = 0

        while i < len(strs[0]):            
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:i]

            i += 1

        return strs[0][:i]