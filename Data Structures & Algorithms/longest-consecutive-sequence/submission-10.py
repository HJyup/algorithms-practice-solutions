class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                curr, count = num, 1

                while curr + 1 in nums:
                    count += 1
                    curr += 1

                res = max(count, res)

        return res