class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # n - k = 7 - 3 = 4
        # just find the smallest possible inner window
        n = len(cardPoints)
        sm = sum(cardPoints)
        m_sm = sm
        window_size = n - k

        curr = 0
        for i in range(window_size):
            curr += cardPoints[i]
        m_sm = min(sm, curr)

        for r in range(window_size, n):
            curr = curr - cardPoints[r - window_size] + cardPoints[r]
            m_sm = min(m_sm, curr)


        return sm - m_sm