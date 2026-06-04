class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans = 0

        def canPack(cap: int) -> bool:
            need, curr = 0, 0

            for w in weights:
                need += 1 if curr + w > cap else 0
                curr = curr + w if curr + w <= cap else w

            return need + 1 <= days

        while low <= high:
            mid = (low + high) // 2

            if canPack(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        