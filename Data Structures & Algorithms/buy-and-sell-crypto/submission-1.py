class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        mn = prices[0]
        for price in prices:
            mn = min(price, mn)
            res = max(res, price - mn)

        return res
        