class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in nums:
            val = 0
            current = num
            if num - 1 not in num_set:
                while current in num_set:
                    current += 1
                    val += 1
            res = max(res, val)

        return res
                

            

