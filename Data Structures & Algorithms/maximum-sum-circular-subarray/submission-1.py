class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Needed for calculation
        total = sum(nums)

        maximum, minimum = nums[0], nums[0]
        curr_max, curr_min = 0, 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)

            maximum = max(maximum, curr_max)
            minimum = min(minimum, curr_min)

        if maximum < 0:
            return maximum

        return max(maximum, total - minimum)