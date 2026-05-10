class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            base_value = target - nums[i]
            if base_value in nums_map:
                return [nums_map[base_value], i]
            nums_map[nums[i]] = i
            
        