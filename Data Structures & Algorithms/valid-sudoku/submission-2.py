from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == '.':
                    continue

                if val in rows[r]:
                    return False

                rows[r].add(val)

                if val in cols[c]:
                    return False

                cols[c].add(val)

                if val in box[(r // 3, c // 3)]:
                    return False

                box[(r // 3, c // 3)].add(val)

        return True
        