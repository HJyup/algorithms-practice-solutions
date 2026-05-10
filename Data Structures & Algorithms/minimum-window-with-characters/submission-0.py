class Solution:
    def check_condition(self, a, b):
        for i in range(len(a)):
            if a[i] < b[i]:
                return False
        return True

    def char_to_index(self, c):
        return ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26

    def minWindow(self, s: str, t: str) -> str:
        res = ""
        check, window = [0] * 52, [0] * 52
        for ch in t:
            check[self.char_to_index(ch)] += 1

        l = 0
        for r in range(len(s)):
            window[self.char_to_index(s[r])] += 1

            while self.check_condition(window, check):
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r+1]
                window[self.char_to_index(s[l])] -= 1
                l += 1
                
            r += 1

        return res