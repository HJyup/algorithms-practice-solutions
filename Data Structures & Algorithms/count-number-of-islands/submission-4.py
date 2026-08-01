from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0

        def bfs(r: int, c: int):
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < 0 or row >= n or col < 0 or col >= m:
                        continue

                    if grid[row][col] == '0':
                        continue

                    grid[row][col] = '0'
                    q.append((row, col))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    bfs(r, c)
                    ans += 1

        return ans