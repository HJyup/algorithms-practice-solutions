from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = 0

        for num in nums:
            freq[num] += 1
            if freq[num] > len(nums) // 2 and freq[num] > res:
                res = num

        return res
        