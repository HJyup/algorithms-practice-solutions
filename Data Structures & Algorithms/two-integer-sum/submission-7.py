class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, num in enumerate(nums):
            if num in diff:
                return [diff[num], i]

            diff[target - num] = i

        return [-1, -1]