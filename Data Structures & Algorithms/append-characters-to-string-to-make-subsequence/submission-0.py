class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # coaching, coding
        # coachcoding
        ans = len(t)

        j = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                ans -= 1
                j += 1

        return ans