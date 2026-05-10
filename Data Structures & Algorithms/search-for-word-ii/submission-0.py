class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        root = Trie()
        res = []

        # Build Trie
        for word in words:
            current = root
            
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = Trie()
                current = current.children[letter]

            current.word = word

        # Recursively Find Words
        def dfs(row, col, node):
            letter = board[row][col]

            if letter not in node.children:
                return None

            next_node = node.children[letter]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[row][col] = '#'
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if not (0 <= new_row < rows) or not (0 <= new_col < cols) or board[new_row][new_col] == '#':
                    continue

                dfs(new_row, new_col, next_node)

            board[row][col] = letter
            return None

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
        