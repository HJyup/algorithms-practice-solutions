class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def checkCondition(row, col):
            return min(row, col) < 0 or row >= rows or col >= cols or grid[row][col] == 0

        def bfs(row, col):
            nonlocal res

            queue = deque()
            queue.append((row, col))
            grid[row][col] = 0
            temp = 1 

            while queue:
                for i in range(0, len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        d_row = dr + r
                        d_col = dc + c
                        if checkCondition(d_row, d_col):
                            continue
                        queue.append((d_row, d_col))
                        grid[d_row][d_col] = 0
                        temp += 1

            res = max(temp, res)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    bfs(i, j)

        return res
        