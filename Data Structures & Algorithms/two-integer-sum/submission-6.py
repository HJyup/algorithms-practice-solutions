class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_target = {}

        for i in range(0, len(nums)):
            target_difference = target - nums[i]
            if target_difference in nums_to_target:
                return [nums_to_target[target_difference], i]
            else:
                nums_to_target[nums[i]] = i
        
        return []