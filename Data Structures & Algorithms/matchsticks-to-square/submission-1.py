class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # The quesiton is about can we divide matchsticks into 4 parts?
        # therefore first check should be is it divisible by 4?
        matchsticks.sort(reverse=True)

        sm = sum(matchsticks)
        n = len(matchsticks)

        if sm % 4 != 0:
            return False
        
        lines = [0] * 4
        line_width = sm // 4


        if line_width < matchsticks[0]:
            return False
            

        def backtrack(i: int) -> bool:
            if i == n:
                return True

            for j in range(4):
                if lines[j] + matchsticks[i] <= line_width:
                    lines[j] += matchsticks[i] 
                    if backtrack(i + 1):
                        return True

                    lines[j] -= matchsticks[i]

            return False

        return backtrack(0)