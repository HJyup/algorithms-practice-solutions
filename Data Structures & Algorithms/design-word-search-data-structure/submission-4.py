class Node:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(node: Node, idx: int):
            if word[idx] != '.' and word[idx] not in node.children:
                return False

            # Last element
            if idx == len(word) - 1:
                if word[idx] == '.':
                    for child in node.children.values():
                        if child.isEnd:
                            return True
                    return False
                return node.children[word[idx]].isEnd

            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
            else:
                if dfs(node.children[word[idx]], idx + 1):
                    return True

            return False

        return dfs(self.root, 0)
