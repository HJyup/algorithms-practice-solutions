class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def isPalindrome(word: str):
            left, right = 0, len(word) - 1
            while left <= right:
                if word[left] != word[right]:
                    return False

                left, right = left + 1, right - 1

            return True

        path = []
        def dfs(start):
            nonlocal res

            if start == n:
                res.append(path[:])
                return None

            for end in range(start, n):
                substring = s[start : end + 1]

                if isPalindrome(substring):
                    path.append(substring)
                    dfs(end + 1)
                    path.pop()

            return None
            
        dfs(0)
        return res
        