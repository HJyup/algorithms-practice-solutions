class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. Mark values that we want to safe.
        # 2. Iterate through matrix marking other 'O'.
        # 3. Remove all safed into 'O' again.
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols):
                return None

            if board[row][col] != 'O':
                return None

            board[row][col] = '#'
            for dr, dc in directions:
                dfs(row + dr, col + dc)

            return None
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Remove all saved valued and change unsaved to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'

                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        return None