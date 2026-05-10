class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0

        st = []
        for i, bar in enumerate(height):
            while st and bar > st[-1][0]:
                bottom, _ = st.pop()
                if st:
                    left, left_idx = st[-1]
                    min_height, width = min(left, bar) - bottom, i - left_idx - 1

                    trapped += min_height * width

            st.append((bar, i))         

        return trapped