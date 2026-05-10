class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0

        for num in st:
            if num - 1 not in st:
                curr, count = num, 0
                while curr in st:
                    curr += 1
                    count += 1
                res = max(count, res)

        return res
