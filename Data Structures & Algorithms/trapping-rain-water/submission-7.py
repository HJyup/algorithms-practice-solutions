class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        left, right = 0, len(height) - 1
        left_mx, right_mx = 0, 0

        while left < right:
            if height[left] < height[right]:
                left_mx = max(left_mx, height[left])
                res += left_mx - height[left]
                left += 1

            else:
                right_mx = max(right_mx, height[right])
                res += right_mx - height[right]
                right -= 1

        return res