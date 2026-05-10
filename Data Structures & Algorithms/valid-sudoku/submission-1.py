from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                block_id = (i // 3) * 3 + (j // 3)

                if (val in rows[i] or val in cols[j] or val in blocks[block_id]):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                blocks[block_id].add(val)

        return True