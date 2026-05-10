class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            s.add(num)

        return len(s) != len(nums)
         