class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):        # Rows
            for j in range(len(matrix[0])):  # Columns
                if matrix[i][j] == target:
                    return True
        return False