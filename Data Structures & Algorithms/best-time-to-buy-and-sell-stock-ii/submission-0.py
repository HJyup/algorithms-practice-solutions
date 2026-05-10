class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        res = 0

        for price in prices:
            if price > mn:
                res += price - mn
                mn = price
            else:
                mn = price

        return res
