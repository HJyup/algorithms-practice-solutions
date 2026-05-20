class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # mark any Parentheses as invalid first
        # then if u found match -> remove them from the stack
        # then go in string adding all chars and omit what u deleted
        st = []

        for i, ch in enumerate(s):
            if ch == '(':
                st.append(('(', i))
            
            elif ch == ')':
                if st and st[-1][0] == '(':
                    st.pop()
                else:
                    st.append((')', i))

        to_remove = { i for _, i in st }
        ans = []

        for i, ch in enumerate(s):
            if i in to_remove:
                continue

            ans.append(ch)

        return ''.join(ans)