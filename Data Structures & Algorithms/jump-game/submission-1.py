class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def jump(idx):
            if idx >= n - 1:
                return True

            value = nums[idx]
            for i in range(1, value + 1):
                if jump(idx + i):
                    return True

            return False

        return jump(0)