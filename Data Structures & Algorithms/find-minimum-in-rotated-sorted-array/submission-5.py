class Solution:
    def findMin(self, nums: List[int]) -> int:
        # check nums[0] and nums[-1] with mid to understand where we have monotonic req
        left, right = 0, len(nums) - 1
        ans = nums[0]

        # nums are unique
        while left <= right:
            mid = (left + right) // 2
            
            # preserved property (monotonic thing)
            if nums[mid] >= nums[left]:
                ans = min(nums[left], ans)
                left = mid + 1
            else:
                ans = min(nums[mid], ans)
                right = mid - 1

        return ans