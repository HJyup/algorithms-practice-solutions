class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        rows, cols = len(board), len(board[0])
        ans = []

        for word in words:
            curr = root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = Node()
                curr = curr.children[letter]
            curr.word = word

        def dfs(row: int, col: int, curr: Node) -> None:
            if row >= rows or row < 0 or col < 0 or col >= cols:
                return None

            if board[row][col] not in curr.children:
                return None

            curr = curr.children[board[row][col]]
            if curr.word:
                ans.append(curr.word)
                curr.word = None # we still explore futher so no returns

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col, curr)
                    seen.remove((new_row, new_col))

            return None

        for row in range(rows):
            for col in range(cols):
                seen.add((row, col))
                dfs(row, col, root)
                seen.remove((row, col))

        return ans