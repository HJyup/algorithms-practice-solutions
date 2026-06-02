class Solution:
    def decodeString(self, s: str) -> str:
        st = [(0, [])]

        i = 0
        while i < len(s):
            if s[i].isdigit():
                digit = 0
                while s[i] != '[':
                    digit = digit * 10 + int(s[i])
                    i += 1

                st.append((digit, []))
            elif s[i] == ']':
                digit, val = st[-1][0], ''.join(st[-1][1])
                st.pop()

                st[-1][1].append(val * digit)
            else:
                st[-1][1].append(s[i])

            i += 1

        return ''.join(st[-1][1])
