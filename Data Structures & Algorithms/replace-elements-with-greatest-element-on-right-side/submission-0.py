class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        suffix = [-1] * len(arr)

        for i in range(len(arr) - 2, -1, -1):
            suffix[i] = max(arr[i + 1], suffix[i + 1])

        return suffix
        