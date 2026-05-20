class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for st in strs:
            length = len(st)
            encoded.append(str(length) + '#' + st)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        def parseDigits(i: int) -> (int, int):
            digit = 0

            while i < len(s) and s[i] != '#':
                digit = digit * 10 + int(s[i])
                i += 1

            return (digit, i + 1) # skipping #

        i = 0
        while i < len(s):
            length, upd_i = parseDigits(i)
            i = upd_i

            decoded.append(s[i : i + length])
            i += length

        return decoded