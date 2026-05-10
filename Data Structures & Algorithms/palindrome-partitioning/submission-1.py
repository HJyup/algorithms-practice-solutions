class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []
        memo = {}

        def isPalindrome(l: int, r: int) -> bool:
            if (l, r) in memo:
                return memo[(l, r)]

            original_l, original_r = l, r
            while l < r:
                if s[l] != s[r]:
                    memo[(original_l, original_r)] = False
                    return False
                l += 1
                r -= 1

            memo[(original_l, original_r)] = True
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
        