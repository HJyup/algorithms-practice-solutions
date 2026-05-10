class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        path = []
        def dfs(opened = n, closed = n):
            nonlocal res
            
            if opened == 0 and closed == 0:
                candidate = ''.join(path)   
                res.append(candidate)

                return None

            if opened != 0:
                path.append('(')
                dfs(opened - 1, closed)
                path.pop()

            if opened < closed:
                path.append(')')
                dfs(opened, closed - 1)
                path.pop()

            return None

        dfs()
        return res
        