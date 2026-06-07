class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # non-decreasing -> increasing / duplicates
        ans = 0

        cook = 0
        for start, time in customers:
            cook = cook if cook > start else start
            cook += time
            ans += max(cook - start, 0)

        return ans / len(customers)