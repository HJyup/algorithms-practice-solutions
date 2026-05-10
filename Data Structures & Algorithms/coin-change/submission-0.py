class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount: int) -> int:
            if amount in memo:
                return memo[amount]
                
            # Base case, if we reached 0 we backtrack
            if amount == 0:
                return 0

            # Initialise the count for each level
            count = float('inf')
            for coin in coins:
                # If it's possible to substrack
                if amount - coin >= 0:
                    # Take the min between current lvl count ( we propagating the result from level to top )
                    count = min(count, 1 + dfs(amount - coin))
            
            memo[amount] = count
            return memo[amount]

        res = dfs(amount)
        return -1 if res == float('inf') else res
