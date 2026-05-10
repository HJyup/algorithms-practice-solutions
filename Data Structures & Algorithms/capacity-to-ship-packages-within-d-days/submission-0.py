class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sm = sum(weights)
        res = sm

        def ship(capacity):
            used_days = 1

            left_capacity = capacity
            for weight in weights:
                if left_capacity - weight < 0:
                    left_capacity = capacity
                    used_days += 1

                left_capacity -= weight

            return used_days <= days

        left, right = max(weights), sm
        while left <= right:
            current_capaciy = (left + right) // 2

            if ship(current_capaciy):
                res = min(current_capaciy, res)
                right = current_capaciy - 1

            else:
                left = current_capaciy + 1

        return res