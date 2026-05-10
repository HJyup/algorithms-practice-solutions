class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # include zero to force stack check all of the heights
        # We are maintaining monotonic increasing stack
        heights.append(0)
        res = 0

        stack = []
        for i, height in enumerate(heights):
            prev = i 

            while stack and height < stack[-1][0]:
                value, prev = stack.pop()
                res = max(value * (i - prev), res)

            stack.append((height, prev))

        return res