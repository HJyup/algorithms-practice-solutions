class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Node()
        n = len(s)
        ans = []

        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Node()
                curr = curr.children[ch]
            curr.word = word

        curr = []
        def dfs(i: int, node: Node):
            if i == n:
                if node is root:
                    ans.append(" ".join(curr[:]))
                return

            if s[i] not in node.children:
                return

            nxt = node.children[s[i]]
            dfs(i + 1, nxt) # continue the current word

            if nxt.word:
                curr.append(nxt.word)
                dfs(i + 1, root)
                curr.pop()

        dfs(0, root)
        return ans