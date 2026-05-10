from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len, t_len = len(s), len(t)
        window, check = defaultdict(int), defaultdict(int)
        res_left, res_right = -1, -1
        res = float('inf')

        count = 0
        for letter in t:
            if letter not in check:
                count += 1   
            check[letter] += 1

        l = 0
        for r in range(s_len):
            char_r = s[r]
            window[char_r] += 1

            # Check count
            if window[char_r] == check[char_r]:
                count -= 1

            while count == 0:
                dst = r - l + 1

                if dst < res:
                    res = dst
                    res_left, res_right = l, r

                char_l = s[l]
                if window[char_l] == check[char_l]:
                    count += 1
                
                window[char_l] -= 1
                l += 1

        return s[res_left : res_right + 1] if res_left != -1 else ""