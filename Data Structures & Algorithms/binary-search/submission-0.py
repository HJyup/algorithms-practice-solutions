from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_point = 0
        end_point = len(nums) - 1

        while start_point <= end_point:
            target_point = (start_point + end_point) // 2
            val = nums[target_point]
            
            if val == target:
                return target_point
            elif val < target:
                start_point = target_point + 1
            else:
                end_point = target_point - 1

        return -1
