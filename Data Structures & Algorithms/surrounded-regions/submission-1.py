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
        
        # Mark safe values
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r, c)

        # Remove all saved valued and change unsaved to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'

                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        return None