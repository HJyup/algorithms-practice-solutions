class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Largest sum -> min(max(sum) -> inside)
        # Two problems:
        # 1. Find the largest min -> Binary Search on Answer
        # 2. Split the subarray with defined limit (we cannot have any subarray exceed it)

        # Split part -> we don't have reocuriing problem (no DP), since 
        # it's not possible to not correctly split array, it's additive operation
        # We can be greedy and just append to split as much as possible (unless the remainaing elements should be as one subarrays)
        n = len(nums)

        def canSplit(limit: int) -> bool:
            segment, curr = 1, 0
            for num in nums:
                if num + curr <= limit:
                    curr += num
                else:
                    segment += 1
                    curr = num

            return segment <= k
        

        low, high = max(nums), sum(nums)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            print(low, high, mid)
            if canSplit(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
