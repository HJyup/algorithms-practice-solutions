class Node:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class PrefixTree:

    def __init__(self):
        self.root = Node()
    

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
        