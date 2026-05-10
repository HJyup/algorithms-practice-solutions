from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0
        for r in range(k - 1, len(nums)):
            res.append(max(nums[l:r + 1]))
            l += 1

        return res

