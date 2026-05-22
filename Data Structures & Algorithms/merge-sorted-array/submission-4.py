class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_1, p_2 = m - 1, n - 1
        curr = len(nums1) - 1

        while p_1 >= 0 and p_2 >= 0:
            if nums1[p_1] > nums2[p_2]:
                nums1[curr] = nums1[p_1]
                p_1 -= 1
            else:
                nums1[curr] = nums2[p_2]
                p_2 -= 1

            curr -= 1

        while p_2 >= 0:
            nums1[curr] = nums2[p_2]
            p_2 -= 1
            curr -= 1

        return nums1
