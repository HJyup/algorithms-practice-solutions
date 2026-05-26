class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        check = [0] * 26
        wnd = [0] * 26

        for ch in s1:
            check[ord(ch) - ord('a')] += 1

        for i in range(len(s1)):
            wnd[ord(s2[i]) - ord('a')] += 1

        if wnd == check:
            return True

        for r in range(len(s1), len(s2)):
            wnd[ord(s2[r]) - ord('a')] += 1
            wnd[ord(s2[r - len(s1)]) - ord('a')] -= 1
            if wnd == check:
                return True

        return False