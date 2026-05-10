class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '*': lambda x, y : x * y,
            '-': lambda x, y : x - y,
            '/': lambda x, y : int(x / y),
            '+': lambda x, y : x + y
        }

        st = []
        for token in tokens:
            if token in operations:
                y, x = st.pop(), st.pop()
                x, y = int(x), int(y)

                res = operations[token](x, y)
                st.append(res)
            else:
                st.append(token)

        return int(st[0])