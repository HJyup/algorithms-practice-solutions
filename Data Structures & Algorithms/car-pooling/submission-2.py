class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # what if didivde each coordinate into actions like a sweep line
        actions = []

        for trip in trips:
            actions.append((trip[1], 1, trip[0]))
            actions.append((trip[2], 0, -trip[0]))

        heapq.heapify(actions)

        current = 0
        while actions:
            value = heapq.heappop(actions)
            print(value)
            current += value[2]

            if current > capacity:
                return False

        return True