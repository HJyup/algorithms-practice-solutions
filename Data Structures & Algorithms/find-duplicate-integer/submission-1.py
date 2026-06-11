class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow pointer solution is fucking crazy ngl.
        # like i get how it works but it's unreal you can actually figure out it on interview
        
        i = 0
        while i < len(nums):
            # swap until we place it
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

            if nums[i] - 1 != i and nums[i] == nums[nums[i] - 1]:
                return nums[i]

            i += 1

        return -1