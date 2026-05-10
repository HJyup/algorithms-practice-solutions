class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            needed_value = target - nums[i]
            if needed_value in d:
                return [d[needed_value], i]
            d[nums[i]] = i
        return []
        