class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        def dfs(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols):
                return None

            if grid[row][col] != '1':
                return None

            grid[row][col] = '#'
            for dr, dc in directions:
                dfs(row + dr, col + dc)

            return None

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands