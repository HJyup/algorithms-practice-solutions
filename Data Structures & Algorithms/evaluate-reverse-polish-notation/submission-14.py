class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in operations:
                x1 = s.pop()
                x2 = s.pop()
                s.append(operations[token](x2, x1))
            else:
                s.append(int(token))
        
        return s[-1]
            