class Solution:
    def char_to_index(self, c):
        return ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = [0] * 52
        window = [0] * 52

        required = 0
        for ch in t:
            idx = self.char_to_index(ch)
            if need[idx] == 0:
                required += 1
            need[idx] += 1

        formed = 0
        left = 0
        res = ""
        
        for right in range(len(s)):
            idx_r = self.char_to_index(s[right])
            window[idx_r] += 1

            if window[idx_r] == need[idx_r]:
                formed += 1

            while formed == required:
                if res == "" or right - left + 1 < len(res):
                    res = s[left:right + 1]

                idx_l = self.char_to_index(s[left])
                window[idx_l] -= 1

                if window[idx_l] < need[idx_l]:
                    formed -= 1

                left += 1

        return res