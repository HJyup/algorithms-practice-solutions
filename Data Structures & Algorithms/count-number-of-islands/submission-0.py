class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if min(row, col) < 0 or row >= rows or col >= cols or grid[row][col] == '0':
                return

            grid[row][col] = '0'
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        return islands
