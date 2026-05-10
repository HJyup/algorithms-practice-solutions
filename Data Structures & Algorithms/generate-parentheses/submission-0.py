class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.count = n

        def dfs(st, opn, cls):
            if opn == self.count and cls == opn:
                self.res.append(st)
                return

            if opn < self.count:
                dfs(st + "(", opn + 1, cls)
            if cls < opn:
                dfs(st + ")", opn, cls + 1)

        
        dfs("", 0, 0)
        return self.res