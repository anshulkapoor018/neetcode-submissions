class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m-1):
            newRow = [1] * n
            for col in range(n-2, -1, -1):
                newRow[col] = newRow[col + 1] + row[col]
            row = newRow
        
        return row[0]