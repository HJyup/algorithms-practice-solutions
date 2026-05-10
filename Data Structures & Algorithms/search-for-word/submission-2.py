class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            found =  (
                dfs(i - 1, j, idx + 1) or
                dfs(i + 1, j, idx + 1) or
                dfs(i, j - 1, idx + 1) or
                dfs(i, j + 1, idx + 1)
            )

            board[i][j] = temp

            return found

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True

        return False
        