class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def dfs(target: int) -> int:
            if target in memo:
                return memo[target]
                
            if target == 0:
                return 0

            if target < 0:
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, dfs(target - coin))

            memo[target] = 1 + res
            return memo[target]

        res = dfs(amount)
        return -1 if res == float('inf') else res