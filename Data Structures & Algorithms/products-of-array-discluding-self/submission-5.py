class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        suffix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        


        