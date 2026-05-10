from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        protected = set()
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and board[row][col] == 'O':
                    q.append((row, col))
                    protected.add((row, col))

        while q:
            row, col = q.popleft()
            for direction in directions:
                dr, dc = direction
                r, c = row + dr, col + dc
                if (
                    0 <= r < rows and
                    0 <= c < cols and
                    board[r][c] == 'O' and
                    (r, c) not in protected
                ):
                    protected.add((r, c))
                    q.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in protected:
                    board[row][col] = 'X'