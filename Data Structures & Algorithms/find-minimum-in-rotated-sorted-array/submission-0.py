class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        v = nums[-1]

        while l <= r:
            m = (l + r) // 2
            v = nums[m]

            if nums[l] > v and nums[r] > v:
                mx = max(nums[l], nums[r])

                if nums[l] == mx:
                    r = m
                else:
                    l = m
            else:
                mn = min(nums[l], nums[r])

                if nums[l] == mn:
                    r = m - 1
                else:
                    l = m + 1


        return v
        