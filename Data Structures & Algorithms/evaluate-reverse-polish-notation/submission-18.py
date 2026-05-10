class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        commands = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for token in tokens:
            if stack and token in commands:
                y = int(stack.pop())
                x = int(stack.pop())

                stack.append(commands[token](x, y))
            else:
                stack.append(token)

        return stack[-1]