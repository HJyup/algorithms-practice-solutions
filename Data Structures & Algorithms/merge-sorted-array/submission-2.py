class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i, j = n - 1, m - 1

        while i >= 0 and j >= 0:
            if nums1[j] < nums2[i]:
                nums1[last] = nums2[i]
                i -= 1
            else:
                nums1[last] = nums1[j]
                j -= 1

            last -= 1

        if i >= 0:
            nums1[: i + 1] = nums2[: i + 1]


        