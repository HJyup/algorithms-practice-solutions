class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))

        else:
            _, prev_min = self.stack[-1]
            self.stack.append((val, min(prev_min, val)))

        return None

    def pop(self) -> None:
        if not self.stack:
            return None

        self.stack.pop()
        return None

    def top(self) -> int:
        if not self.stack:
            return -1

        current, _ = self.stack[-1]
        return current
        

    def getMin(self) -> int:
        if not self.stack:
            return -1

        _, current = self.stack[-1]
        return current
        
