class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for st in strs:
            length = len(st)
            encoded.append(str(length) + '#' + st)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            digit = 0

            while i < len(s) and s[i] != '#':
                digit = digit * 10 + int(s[i])
                i += 1

            i += 1
            decoded.append(s[i : i + digit])
            i += digit

        return decoded