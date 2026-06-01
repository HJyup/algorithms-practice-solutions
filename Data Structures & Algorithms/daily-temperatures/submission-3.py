class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        # general idea: maintain stack in a way that all ur answers should be 0
        ans = [0] * len(temperatures)
        st = []

        # you update (invariant) ONLY if you enounter bigger value, therefore to maintain
        # only zeros u need decreasing order. (monotonic decreasing stack)
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                ans[st[-1]] = i - st[-1]
                st.pop()
            # append value after validating invariant
            st.append(i)

        return ans
        