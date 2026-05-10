class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        length = len(s)
        longest = 0

        left, freq = 0, 0
        for right in range(length):
            count[ord(s[right]) - ord('A')] += 1
            freq = max(freq, count[ord(s[right]) - ord('A')])

            while left < right and right - left + 1 - freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest