class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # The quesiton is about can we divide matchsticks into 4 parts?
        # therefore first check should be is it divisible by 4?
        matchsticks.sort(reverse=True)
        SIDES = 4

        sm = sum(matchsticks)
        n = len(matchsticks)

        if sm % SIDES != 0:
            return False
        
        lines = [0] * SIDES
        line_width = sm // SIDES


        if line_width < matchsticks[0]:
            return False
            

        def backtrack(i: int) -> bool:
            if i == n:
                return True

            for j in range(SIDES):
                if j > 0 and lines[j] == lines[j-1]:
                    continue

                if lines[j] + matchsticks[i] <= line_width:
                    lines[j] += matchsticks[i] 
                    if backtrack(i + 1):
                        return True

                    lines[j] -= matchsticks[i]

            return False

        return backtrack(0)