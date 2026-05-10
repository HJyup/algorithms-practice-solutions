class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0

        mn = prices[0]
        for price in prices:
            mx = max(mx, price - mn)
            mn = min(mn, price)

        return mx
        