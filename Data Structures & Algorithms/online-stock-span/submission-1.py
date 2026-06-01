class StockSpanner:

    def __init__(self):
        self.st = []

    def _append(self, val: int) -> None:
        span = 0

        while self.st and self.st[-1][1] <= val:
            span += self.st[-1][0]
            self.st.pop()

        self.st.append((span + 1, val))

    def next(self, price: int) -> int:
        # append value to the stack maintaining property
        self._append(price)
        return self.st[-1][0]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)