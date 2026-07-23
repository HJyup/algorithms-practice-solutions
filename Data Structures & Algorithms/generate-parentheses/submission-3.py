class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        curr = []
        def dfs(op: int, cl: int):
            if len(curr) == n * 2:
                res.append(''.join(curr))
                return

            if op != 0:
                curr.append('(')
                dfs(op - 1, cl)
                curr.pop()

            if op < cl:
                curr.append(')')
                dfs(op, cl - 1)
                curr.pop()

        dfs(n, n)
        return res