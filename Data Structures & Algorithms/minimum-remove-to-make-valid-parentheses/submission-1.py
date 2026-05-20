class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # mark any Parentheses as invalid first
        # then if u found match -> remove them from the stack
        # then go in string adding all chars and omit what u deleted
        st = []
        to_remove = set()

        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            
            elif ch == ')':
                if st:
                    st.pop()
                else:
                    to_remove.add(i)

        to_remove.update(set(st))
        ans = []

        for i, ch in enumerate(s):
            if i in to_remove:
                continue

            ans.append(ch)

        return ''.join(ans)