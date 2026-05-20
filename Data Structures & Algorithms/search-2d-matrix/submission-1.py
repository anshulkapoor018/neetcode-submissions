class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        # -----------------------------------
        # STEP 1:
        # Find which row could contain target
        # -----------------------------------

        top = 0
        bottom = rows - 1

        while top <= bottom:

            row = (top + bottom) // 2

            # Target is bigger than this row's max value
            # so search lower rows
            if target > matrix[row][cols - 1]:
                top = row + 1

            # Target is smaller than this row's min value
            # so search upper rows
            elif target < matrix[row][0]:
                bottom = row - 1

            # Target must exist in this row range
            else:
                break

        # If no valid row found
        if top > bottom:
            return False

        # Row where target could exist
        row = (top + bottom) // 2

        # -----------------------------------
        # STEP 2:
        # Binary search inside selected row
        # -----------------------------------

        left = 0
        right = cols - 1

        while left <= right:

            mid = (left + right) // 2

            # Found target
            if matrix[row][mid] == target:
                return True

            # Search left half
            elif matrix[row][mid] > target:
                right = mid - 1

            # Search right half
            else:
                left = mid + 1

        return False