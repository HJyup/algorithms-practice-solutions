class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Thoughts:
        # - Invariant is increasing. We cannot conclude final rectangle from the current one
        # if we can still extend it. (Idea why monotonic increasing stack is used)
        # - The width can be conlcuded from the left AND right. so the bruteforce is pointer
        # for each bar and try to extend to the left AND right.
        # Since the stack is increasing, we can safely push "start" index to the left to 
        # make calculation of the left part in one pass (if it was increasing, so current bar
        # easily can be extended to the left as well just by swapping index).
        # - Adding 0 to the end breaks the invariant calculating all values, so 
        # if all values are increasing, we can still calculate it
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