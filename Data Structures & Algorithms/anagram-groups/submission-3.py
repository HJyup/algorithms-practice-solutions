from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we need to somehow encode them to group. we dont care about order.
        # fist solution is to sort it
        # second solution is to encode via 26 letters since we know
        # made up of lowercase English letters
        dictionary = defaultdict(list)

        def encode_word(word):
            encoding = [0] * 26
            for letter in word:
                encoding[ord(letter) - ord('a')] += 1

            return tuple(encoding)

        for word in strs:
            encoding = encode_word(word)
            dictionary[encoding].append(word)

        result = dictionary.values()
        return list(result)
        