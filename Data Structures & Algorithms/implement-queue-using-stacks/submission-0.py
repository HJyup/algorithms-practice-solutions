class MyQueue:
    def __init__(self):
        self.fst = []
        self.snd = []

    def push(self, x: int) -> None:
        self.fst.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1

        if not self.snd:
            while self.fst:
                self.snd.append(self.fst.pop())

        return self.snd.pop()
        

    def peek(self) -> int:
        if self.empty():
            return -1

        if self.snd:
            return self.snd[-1]

        return self.fst[0]

    def empty(self) -> bool:
        return not self.fst and not self.snd


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()