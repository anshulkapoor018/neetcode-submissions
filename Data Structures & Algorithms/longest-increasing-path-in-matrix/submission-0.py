class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # top down DFS + memo
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c, prev):
            # boundary
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            # explore all 4 directions
            best = 1
            best = max(best, 1 + dfs(r + 1, c, matrix[r][c]))
            best = max(best, 1 + dfs(r - 1, c, matrix[r][c]))
            best = max(best, 1 + dfs(r, c+1, matrix[r][c]))
            best = max(best, 1 + dfs(r, c-1, matrix[r][c]))
            
            memo[(r, c)] = best
            return best
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        
        return res
