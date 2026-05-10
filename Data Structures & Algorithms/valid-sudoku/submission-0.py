from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list);
        cols = defaultdict(list);
        blocks = defaultdict(list)

        for i in range(9):
            for j in range(9):
                block_id = (i // 3) * 3 + (j // 3)
                val = board[i][j]

                if val == ".":
                    continue

                if val in blocks[block_id]:
                    return False
                blocks[block_id].append(val)

                if rows[i] and val in rows[i]:
                    return False
                rows[i].append(val)

                if cols[j] and val in cols[j]:
                    return False
                cols[j].append(val)
        
        return True
            
        
        