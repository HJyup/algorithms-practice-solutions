class StockSpanner:

    def __init__(self):
        self.st = []
        self.size = 0

    def _append(self, val: int) -> None:
        self.size += 1
        prev = self.size

        while self.st and self.st[-1][1] <= val:
            prev = self.st[-1][0]
            self.st.pop()

        self.st.append((prev, val))

    def next(self, price: int) -> int:
        # append value to the stack maintaining property
        self._append(price)
        return self.size - self.st[-1][0] + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)