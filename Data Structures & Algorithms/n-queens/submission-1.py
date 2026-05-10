class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        pos_d, neg_d = set(), set()

        board = [['.'] * n for _ in range(n)]
        def dfs(row):
            nonlocal res

            if row == n:
                res.append([''.join(row) for row in board])
                return None

            for col in range(n):
                if col in cols:
                    continue

                if (row + col) in pos_d or (row - col) in neg_d:
                    continue

                cols.add(col)
                pos_d.add(row + col), neg_d.add(row - col)
                board[row][col] = 'Q'

                dfs(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                pos_d.remove(row + col), neg_d.remove(row - col)

            return None

        dfs(0)
        return res