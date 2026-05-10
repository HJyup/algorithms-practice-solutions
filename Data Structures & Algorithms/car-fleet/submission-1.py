class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        init = list(zip(position, speed))
        init.sort(reverse=True)

        stack = []
        times = [(target - position) / speed for position, speed in init]

        for time in times:
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)