from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        start = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    start.append((r, c))

        q = deque(start)

        while q:
            sr, sc = q.popleft()

            for dr, dc in directions:
                r, c = sr + dr, sc + dc
                if not (0 <= r < rows) or not (0 <= c < cols):
                    continue

                if grid[r][c] != INF:
                    continue

                grid[r][c] = grid[sr][sc] + 1
                q.append((r, c))

        return None