class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                val = 1

                while current + 1 in num_set:
                    current += 1
                    val += 1

                res = max(res, val)

        return res
                

            

