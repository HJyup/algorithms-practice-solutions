class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for _ in range(n)]
        cols, d_mj, d_mn = set(), set(), set()
        res = []

        def place_queen(r, c):
            cols.add(c)
            grid[r][c] = 'Q'
            d_mj.add(r - c)
            d_mn.add(r + c)

        def remove_queen(r, c):
            cols.remove(c)
            grid[r][c] = '.'
            d_mj.remove(r - c)
            d_mn.remove(r + c)

        def dfs(r: int):
            if r == n:
                res.append([''.join(row) for row in grid])
                return

            for c in range(n):
                if c in cols or r - c in d_mj or r + c in d_mn:
                    continue

                place_queen(r, c)
                dfs(r + 1)
                remove_queen(r, c)

        dfs(0)
        return res