class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(0, len(nums)):
            res = target - nums[i]
            if res in dic:
                return [dic[res], i]
            dic[nums[i]] = i

        