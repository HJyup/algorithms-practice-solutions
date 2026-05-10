class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], []
        left_mul, right_mul = 1, 1

        for i in range(len(nums)):
            left_mul *= nums[i]
            prefix.append(left_mul)

            right_mul *= nums[len(nums) - 1 - i]
            postfix.append(right_mul)

        res = []
        for i in range(len(nums)):
            prefix_val = prefix[i - 1] if i != 0 else 1
            postfix_val = postfix[-2 - i] if i != len(nums) - 1 else 1
            res.append(prefix_val * postfix_val)

        return res



        