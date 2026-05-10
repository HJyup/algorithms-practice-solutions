class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0
        heights.append(0)

        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                height = heights[st.pop()]
                width = i if not st else i - st[-1] - 1

                res = max(res, height * width)

            st.append(i)

        return res