class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        if not digits:
            return []

        def dfs(idx, combs):
            if idx == len(digits):
                res.append(combs)
                return

            for letter in digit_to_letters[digits[idx]]:
                dfs(idx + 1, combs + letter)

        dfs(0, "")
        return res
