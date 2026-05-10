class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        st = []
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)

        return res