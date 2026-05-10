class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def dfs(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols):
                return 0

            if grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) +dfs(row, col + 1) + dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current = dfs(r, c)
                    area = max(current, area)

        return area
        