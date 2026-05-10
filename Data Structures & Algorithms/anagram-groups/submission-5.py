from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        letter_position = lambda x: ord(x) - ord('a')

        for word in strs:
            group = [0] * 26

            for ch in word:
                group[letter_position(ch)] += 1

            groups[tuple(group)].append(word)

        return list(groups.values())