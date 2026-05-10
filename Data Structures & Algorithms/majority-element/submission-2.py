from collections import defaultdict

class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     freq = defaultdict(int)

    #     for num in nums:
    #         freq[num] += 1
    #         if freq[num] > len(nums) // 2:
    #             return num

    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num

            count += (1 if num == res else -1)

        return res