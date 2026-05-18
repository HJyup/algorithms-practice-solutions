import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Right - pivot element
        # Left - left (taking small elements)

        def partition(left: int, pivot: int) -> int:
            if left >= pivot:
                return left

            rand_idx = random.randint(left, pivot)
            nums[rand_idx], nums[pivot] = nums[pivot], nums[rand_idx]
            
            right = pivot - 1

            while left <= right:
                if nums[left] > nums[pivot]:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1

                else:
                    left += 1

            nums[pivot], nums[left] = nums[left], nums[pivot]
            return left

        def quick(left, right):
            if left >= right:
                return None

            idx = partition(left, right)
            quick(left, idx - 1)
            quick(idx + 1, right)

            return None

        quick(0, len(nums) - 1)
        return nums