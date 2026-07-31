class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0

        ans = 0

        time = customers[0][0]
        for start, wait in customers:
            time = max(start, time)

            ans += (time + wait) - start
            time += wait

        return ans / len(customers)