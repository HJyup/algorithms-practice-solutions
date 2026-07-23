class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(idx: int, row: int, col: int) -> bool:
            if board[row][col] != word[idx] or (row, col) in seen:
                return False

            if idx == len(word) - 1 and board[row][col] == word[idx]:
                return True

            seen.add((row, col))
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    if dfs(idx + 1, r, c):
                        return True

            seen.remove((row, col))
            return False

        for r in range(rows):
            for c in range(cols):
                seen = set()
                if dfs(0, r, c):
                    return True

        return False