class Solution:
    def isPathCrossing(self, path: str) -> bool:
        actions = {
            'N': (0, 1),
            'S': (0, -1),
            'W': (1, 0),
            'E': (-1, 0)
        }
        seen = {(0, 0)}

        x, y = 0, 0
        for action in path:
            x, y = x + actions[action][0], y + actions[action][1]
            if (x, y) in seen:
                return True

            seen.add((x, y))

        return False
        