class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def isSafe(row, col):
            if col in cols or row + col in pos_diagonal or row - col in neg_diagonal:
                return False
            return True

        def placeQueen(row, col):
            board[row][col] = 'Q'
            pos_diagonal.add(row + col)
            neg_diagonal.add(row - col)
            cols.add(col)

        def removeQueen(row, col):
            board[row][col] = '.'
            pos_diagonal.remove(row + col)
            neg_diagonal.remove(row - col)
            cols.remove(col)

        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in board])

            for col in range(n):
                if isSafe(row, col):
                    placeQueen(row, col)
                    dfs(row + 1)
                    removeQueen(row, col)

        dfs(0)
        return res
        