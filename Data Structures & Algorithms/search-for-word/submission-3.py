class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def dfs(r, c, i):
            if i == n:
                return True

            if not (0 <= r < rows) or not (0 <= c < cols):
                return False

            if i > n or board[r][c] != word[i]:
                return False

            i += 1
            prev, board[r][c] = board[r][c], '#'
            res = dfs(r + 1, c, i) or dfs(r - 1, c, i) or dfs(r, c + 1, i) or dfs(r, c - 1, i)
            board[r][c] = prev

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False