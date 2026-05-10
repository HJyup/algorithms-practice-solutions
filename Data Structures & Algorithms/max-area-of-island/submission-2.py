class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (
                row < 0 or row == rows or
                col < 0 or col == cols or
                grid[row][col] == 0 or
                (row, col) in visited
            ):
                return 0

            visited.add((row, col))
            return (
                1 + dfs(row + 1, col) + 
                dfs(row - 1, col) + 
                dfs(row, col + 1) +
                dfs(row, col - 1)
            )

        for row in range (rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    res = max(res, dfs(row, col))

        return res
        
        