class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]

        current.is_word = True
        return None

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(current, i):
            if i == n:
                return current.is_word

            letter = word[i]

            if letter == '.':
                for child in current.children.values():
                    if dfs(child, i + 1):
                        return True
                        
                return False
            else:
                if letter not in current.children:
                    return False

                return dfs(current.children[letter], i + 1)

            return False

        return dfs(self.root, 0)
