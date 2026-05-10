class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Split array in half.
        # Merge them together

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            merged = []

            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                
                else:
                    merged.append(arr2[j])
                    j += 1

            while i < len(arr1):
                merged.append(arr1[i])
                i += 1

            while j < len(arr2):
                merged.append(arr2[j])
                j += 1

            return merged

        def mergeSort(arr: List[int]):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        return mergeSort(nums)
