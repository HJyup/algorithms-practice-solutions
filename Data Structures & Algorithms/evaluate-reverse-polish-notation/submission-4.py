class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        for token in tokens:
            if token in operations:
                val2 = int(st.pop())
                val1 = int(st.pop())
                st.append(operations[token](val1, val2))
            else:
                st.append(int(token))
        
        return st[0]