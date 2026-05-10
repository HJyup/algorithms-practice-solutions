class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, sm = float('inf'), 0
        l = 0
        for r in range(len(nums)):
            sm += nums[r]
            while sm >= target:
                res = min(res, r - l + 1)
                sm -= nums[l]
                l += 1            

        return 0 if res == float('inf') else res
        