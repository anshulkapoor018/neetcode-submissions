class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down
        # 2 choices : move right or move down at each cell
        memo = {}

        def dfs(row, col):
            if row == m or col == n:
                return 0 
            
            if row == m-1 and col == n-1:
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            down = dfs(row+1, col)
            right = dfs(row, col+1)

            memo[(row, col)] = down + right
            return memo[(row, col)]
        
        return dfs(0, 0)
        
        #bottom up
        row = [1] * n

        for _ in range(m-1):
            newRow = [1] * n
            for col in range(n-2, -1, -1):
                newRow[col] = newRow[col + 1] + row[col]
            row = newRow
        
        return row[0]