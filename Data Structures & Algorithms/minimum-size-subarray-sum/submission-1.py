class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')

        l = 0
        sm = 0
        for r in range(len(nums)):
            sm += nums[r]
            while sm >= target:
                ans = min(r - l + 1, ans)
                sm -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0