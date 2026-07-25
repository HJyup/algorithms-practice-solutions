class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)

        WALLS_COUNT = 4
        sm = sum(matchsticks)
        n = len(matchsticks)

        if sm % WALLS_COUNT != 0:
            return False

        target = sm // WALLS_COUNT
        seen = set() # has to be == to matchsticks if we reach 4

        if matchsticks[0] > target:
            return False

        def dfs(wall: int, curr: int) -> bool:
            if wall == WALLS_COUNT:
                return True

            for i in range(n):
                if i not in seen:
                    new_curr = curr + matchsticks[i]
                    if new_curr > target:
                        continue

                    seen.add(i)
                    if new_curr == target:
                        if dfs(wall + 1, 0):
                            return True

                    elif dfs(wall, new_curr):
                        return True

                    seen.remove(i)

            return False

        return dfs(1, 0)