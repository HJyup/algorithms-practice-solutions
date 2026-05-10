from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        steps = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            n = len(q)
            for _ in range(n):
                row, col = q.popleft()
                for direction in directions:
                    dr, dc = direction
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 2147483647:
                        grid[r][c] = steps
                        q.append((r, c))
            steps += 1
        