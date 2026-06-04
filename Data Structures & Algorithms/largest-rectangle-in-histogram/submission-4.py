class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ans = 0
        st = []

        for r, h in enumerate(heights):
            start = r
            
            while st and heights[st[-1]] >= h:
                start = st.pop()
                ans = max(ans, (r - start) * heights[start])
                heights[start] = h

            st.append(start)

        return ans