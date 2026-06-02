class Solution:
    def decodeString(self, s: str) -> str:
        st = [(0, [])]
        current_digit = 0

        for ch in s:
            if ch.isdigit():
                current_digit = current_digit * 10 + int(ch)
            elif ch == '[':
                st.append((current_digit, []))
                current_digit = 0
            elif ch == ']':
                digit, val = st.pop()
                st[-1][1].append(''.join(val) * digit)
            else:
                st[-1][1].append(ch)

        return ''.join(st[-1][1])
