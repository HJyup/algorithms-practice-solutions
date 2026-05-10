class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        for num in nums:
            if num - 1 not in s:
                curr, count = num, 1
                while curr in s:
                    res = max(res, count)
                    count += 1
                    curr += 1

        return res
                

            

