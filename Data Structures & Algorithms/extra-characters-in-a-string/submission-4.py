class Node:
    def __init__(self, isEnd = False):
        self.children = {}
        self.isEnd = isEnd

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        memo = {}
        root = Node()

        for word in dictionary:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Node()
                curr = curr.children[ch]
            curr.isEnd = True

        def dfs(i: int):
            if i in memo:
                return memo[i]

            if i == n:
                return 0

            ans = 1 + dfs(i + 1) # O(n)
            j, curr = i, root

            while j < n and s[j] in curr.children:
                curr = curr.children[s[j]]
                j += 1
                if curr.isEnd:
                    ans = min(ans, dfs(j)) 

            memo[i] = ans
            return memo[i]

        return dfs(0)