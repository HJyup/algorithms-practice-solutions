class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        product, left = 1, 0
        for right in range(n):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1

            count += right - left + 1

        return count
        