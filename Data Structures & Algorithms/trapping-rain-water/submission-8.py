class Solution:
    def trap(self, height: List[int]) -> int:
        res = [0] * len(height)

        mx = height[0]
        for i in range(len(height)):
            mx = max(mx, height[i])
            res[i] = max(mx - height[i], 0)

        mx = height[-1]
        for i in range(len(height) -1, -1, -1):
            mx = max(mx, height[i])
            
            diff = max(mx - height[i], 0)
            if diff >= 0:
                res[i] = min(res[i], diff)

        return sum(res)