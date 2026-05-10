class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(re.findall(r"[a-z0-9]", s.lower()))

        l, r = 0, len(new_s) - 1
        while l <= r:
            if new_s[l] != new_s[r]:
                return False

            l += 1
            r -= 1

        return True