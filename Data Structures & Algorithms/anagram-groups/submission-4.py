from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        index = lambda x: ord(x) - ord('a')

        for word in strs:
            code = [0] * 26

            for ch in word:
                code[index(ch)] += 1

            freq[tuple(code)].append(word)

        return list(freq.values())