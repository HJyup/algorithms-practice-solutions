class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set()
        
        for num in nums:
            s.add(num)

        for num in nums:
            curr, count = num, 1
            while curr in s:
                res = max(res, count)
                count += 1
                curr += 1

        return res
                

            

