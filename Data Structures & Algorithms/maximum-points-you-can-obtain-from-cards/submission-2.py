class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        prefix, suffix = [0] * n, [0] * (n + 1)
        
        curr = 0
        for i in range(n):
            prefix[i] = cardPoints[i] + curr
            curr += cardPoints[i]

        curr = 0
        for i in range(n - 1, -1, -1):
            suffix[i] = cardPoints[i] + curr
            curr += cardPoints[i]

        ans = suffix[n - k]
        for i in range(k):
            ans = max(ans, prefix[i] + suffix[n - k + i + 1])

        return ans