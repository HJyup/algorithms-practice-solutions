class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 0

        while self.st and self.st[-1][1] <= price:
            span += self.st[-1][0]
            self.st.pop()

        self.st.append((span + 1, price))
        return span + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)