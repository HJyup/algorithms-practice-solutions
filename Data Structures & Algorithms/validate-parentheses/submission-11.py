class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in close_to_open:
                if not st or st[-1] != close_to_open[ch]:
                    return False

                st.pop()
            else:
                st.append(ch)

        return len(st) == 0