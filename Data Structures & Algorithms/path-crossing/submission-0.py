class Solution:
    def isPathCrossing(self, path: str) -> bool:
        actions = {
            'N': (0, 1),
            'S': (0, -1),
            'W': (1, 0),
            'E': (-1, 0)
        }
        seen = {(0, 0)}

        current = (0, 0)
        for action in path:
            current = (current[0] + actions[action][0], current[1] + actions[action][1])
            if current in seen:
                return True

            seen.add(current)
            
        return False
        