class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find corresponding row
        # (left search)
        n, m = len(matrix), len(matrix[0])

        left, right = 0, n - 1
        row = 0

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target:
                row = mid
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False