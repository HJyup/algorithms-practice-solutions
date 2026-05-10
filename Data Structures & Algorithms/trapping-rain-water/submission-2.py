class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        h = 0

        while l < r:
            min_h = min(height[l], height[r])
            h = max(h, min_h)
            if height[l] == min_h:
                l += 1
                res += max(0, h - height[l])
            else:
                r -= 1
                res += max(0, h - height[r])

        return res