class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        l, r = 0, len(heights) - 1
        while l < r:
            square = min(heights[l], heights[r]) * (r - l)
            if square > result:
                result = square

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result

            
        