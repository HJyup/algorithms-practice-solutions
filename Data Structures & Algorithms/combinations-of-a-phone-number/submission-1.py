class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        n = len(digits)
        res = []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        path = []
        def dfs(start):
            nonlocal res

            if start == n:
                word = ''.join(path)
                res.append(word)

                return None

            for letter in phone[digits[start]]:
                path.append(letter)
                dfs(start + 1)
                path.pop()

            return None

        dfs(0)
        return res