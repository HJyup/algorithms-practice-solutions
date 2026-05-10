class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        path = []
        def backtrack(o: int, c: int) -> None:
            if (o + c) // 2 == n:
                res.append(''.join(path))
                return None

            if o != n:
                path.append('(')
                backtrack(o + 1, c)
                path.pop()

            if c < o:
                path.append(')')
                backtrack(o, c + 1)
                path.pop()

            return None

        backtrack(0, 0)
        return res