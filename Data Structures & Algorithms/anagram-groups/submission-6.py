class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tuple as a list key (lowercase English letters)
        # sort - worse time

        def buildKey(word):
            key = [0 for _ in range(26)]

            for ch in word:
                idx = ord(ch) - ord('a')
                key[idx] += 1

            return tuple(key)

        groups = {}

        for i, word in enumerate(strs):
            key = buildKey(word)
            if key not in groups:
                groups[key] = []

            # A lot of references (in leetcode spes.) uses index storage
            # instead of value (for "memory benefit"). However, it's not true
            # Python stores references to strings. 
            # so appending a string costs the same as appending an index (IADS course).
            # (IADS course, lol). 
            groups[key].append(word)

        return list(groups.values())