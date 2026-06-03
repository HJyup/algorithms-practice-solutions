class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time to get to the target: (target - position) / speed
        vals = sorted(list(zip(position, speed)), reverse=True)
        time = [(target - pos) / speed for pos, speed in vals]
        st = []

        for t in time:
            if not st or t > st[-1]:
                st.append(t)

        return len(st)