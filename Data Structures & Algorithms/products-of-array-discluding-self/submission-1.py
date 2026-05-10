class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        left_mul, right_mul = 1, 1

        for i in range(len(nums)):
            left_mul *= nums[i]
            right_mul *= nums[len(nums) - 1 - i]
            
            prefix.append((left_mul, right_mul))

        res = []
        for i in range(len(nums)):
            prefix_val = prefix[i - 1][0] if i != 0 else 1
            postfix_val = prefix[-2 - i][1] if i != len(nums) - 1 else 1
            res.append(prefix_val * postfix_val)

        return res



        