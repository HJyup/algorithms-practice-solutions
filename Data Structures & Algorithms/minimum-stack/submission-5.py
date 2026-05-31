class MinStack:

    def __init__(self):
        self.st = []
        self.mn = []
        

    def push(self, val: int) -> None:
        if not self.mn:
            self.mn.append(val)
        else:
            self.mn.append(min(self.mn[-1], val))

        self.st.append(val)
        return None
        

    def pop(self) -> None:
        self.mn.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mn[-1]