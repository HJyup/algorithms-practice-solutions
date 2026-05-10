class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        sufix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            sufix[i] = nums[i + 1] * sufix[i + 1]

        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = sufix[i] * prefix[i]

        return res
        


        