class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for num in nums:
            if num in vals:
                return True
            vals.add(num)

        return False
         