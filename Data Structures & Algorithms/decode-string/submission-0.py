class Solution:
    def decodeString(self, s: str) -> str:
        digits, st = [], [[]]

        i = 0
        while i < len(s):
            if s[i].isdigit():
                digit = 0

                while s[i] != '[':
                    digit = digit * 10 + int(s[i])
                    i += 1

                digits.append(digit)
                st.append([])
            elif s[i] == ']':
                val = ''.join(st[-1])
                st.pop()

                st[-1].append(val * digits[-1])
                digits.pop()
            else:
                st[-1].append(s[i])

            i += 1

        return ''.join(st[-1])
