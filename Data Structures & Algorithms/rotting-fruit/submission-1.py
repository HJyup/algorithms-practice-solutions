from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        count = -1
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while q:
            count += 1
            n = len(q)
            for _ in range(n):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
                        continue
                    
                    q.append((r, c))
                    grid[r][c] = 2
                    fresh -= 1



        return count if fresh == 0 else -1
        