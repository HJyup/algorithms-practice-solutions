class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def rotate(low: int, high: int) -> None:
            if low >= high:
                return None

            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

            return None

        # rotate the whole array
        rotate(0, n - 1)

        # rotate first part
        rotate(0, k - 1)
        rotate(k, n - 1)

        return None