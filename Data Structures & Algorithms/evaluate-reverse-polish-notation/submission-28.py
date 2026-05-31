class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda b, a: a + b,
            '-': lambda b, a: a - b,
            '*': lambda b, a: a * b,
            '/': lambda b, a: int(a / b)
        }
        st = []

        for t in tokens:
            if t in ops:
                st.append(ops[t](st.pop(), st.pop()))
            else:
                st.append(int(t))

        return st[-1]