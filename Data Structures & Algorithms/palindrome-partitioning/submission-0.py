class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []

        def isPalindrome(l: str, r: str) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(idx):
            # base case when all values are used
            if idx == len(s):
                res.append(parts[:])
                return
            
            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    parts.append(s[idx:i+1])
                    dfs(i + 1)
                    parts.pop() 


        dfs(0)
        return res
        