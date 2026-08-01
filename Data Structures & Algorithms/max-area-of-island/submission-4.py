class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0

        def dfs(r: int, c: int) -> int:
            grid[r][c] = 0
            ans = 1

            for dr, dc in directions:
                row, col = r + dr, c + dc

                if row < 0 or row >= n or col < 0 or col >= m:
                    continue

                if grid[row][col] == 0:
                    continue

                grid[row][col] = 0
                ans += dfs(row, col)

            return ans

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans