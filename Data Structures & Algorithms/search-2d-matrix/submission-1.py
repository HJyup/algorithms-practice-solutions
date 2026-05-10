from typing import List

class Solution:
    def searchRow(self, matrix: List[List[int]], target: int) -> int:
        start_point = 0
        end_point = len(matrix) - 1
        while start_point <= end_point:
            target_point = (start_point + end_point) // 2 
            val = matrix[target_point][0]
            
            if val == target:
                return target_point
            elif val < target:
                start_point = target_point + 1
            else:
                end_point = target_point - 1

        return end_point

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.searchRow(matrix, target)
        if row < 0 or row >= len(matrix):
            return False
        
        start_point = 0
        end_point = len(matrix[row]) - 1
        while start_point <= end_point:
            target_point = (start_point + end_point) // 2 
            val = matrix[row][target_point]
            
            if val == target:
                return True
            elif val < target:
                start_point = target_point + 1
            else:
                end_point = target_point - 1

        return False
