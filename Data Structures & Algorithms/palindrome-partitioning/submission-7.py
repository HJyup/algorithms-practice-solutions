class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        def palindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        curr = []
        def dfs(i: int):
            if i >= n:
                ans.append(curr[:])
                return

            for j in range(i, n):
                if palindrome(i, j):
                    curr.append(s[i: j + 1])
                    dfs(j + 1)
                    curr.pop()

            return

        dfs(0)
        return ans