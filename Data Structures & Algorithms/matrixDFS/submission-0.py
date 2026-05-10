class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visited):
            rows, cols = len(grid), len(grid[0])
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r, c) in visited:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1

            visited.add((r, c))

            count = 0
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove((r, c))
            return count

        return dfs(grid, 0, 0, set())
                    

        