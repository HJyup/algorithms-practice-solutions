class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        hold = prices[0]
        for price in prices[1:]:
            # 1. prices goes down -> just update hold
            # 2. price goes up -> sell and take
            if price - hold > 0:
                ans += price - hold
                hold = price

            else:
                hold = min(price, hold)

        return ans
