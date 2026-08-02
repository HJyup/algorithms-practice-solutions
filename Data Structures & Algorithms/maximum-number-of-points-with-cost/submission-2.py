class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = [0] * m

        for r in range(n - 1, -1, -1):
            new_row = []

            for c_1 in range(m):
                val = points[r][c_1]
                mx = 0

                for c_2 in range(m):
                    mx = max(dp[c_2] + val - abs(c_1 - c_2), mx)
                
                new_row.append(mx)

            dp = new_row

        return max(dp)