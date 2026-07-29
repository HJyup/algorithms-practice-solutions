class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sweep = []

        for trip in trips:
            sweep.extend([(trip[1], trip[0]), (trip[2], -trip[0])])

        sweep.sort()
        curr = 0
        print(sweep)
        for _, cap in sweep:
            curr += cap
            if curr > capacity:
                return False

        return True

