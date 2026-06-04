class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on answer
        # we wanna find can we eat given amount of hpurs
        if len(piles) > h:
            return -1

        # because the abosulte max is when everything can be eaten in one turn
        low, high = 1, max(piles)
        ans = 0

        # using canEat(val) -> bool transform search space into
        # false, ..., false, true, true, .... true
        # we need ot find very first true (binary search right mod)

        def canEat(speed: int) -> bool:
            time = 0
            for pile in piles:
                val = pile / speed
                time += int(val) + 1 if val != int(val) else int(val)
            return time <= h

        while low <= high:
            mid = (low + high) // 2

            if canEat(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans