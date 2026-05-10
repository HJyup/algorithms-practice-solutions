class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        SIDES = 4

        length = sum(matchsticks) // SIDES
        sides = [0] * SIDES

        if sum(matchsticks) / 4 != length:
            return False

        matchsticks.sort(reverse=True)

        def backtrack(i: int):
            if i == n:
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    sides[j] -= matchsticks[i]
            
            return False

        return backtrack(0)
        