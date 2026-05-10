class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left

            if heights[left] < heights[right]:
                res = max(res, heights[left] * width)
                left += 1
            else:
                res = max(res, heights[right] * width)
                right -= 1

        return res