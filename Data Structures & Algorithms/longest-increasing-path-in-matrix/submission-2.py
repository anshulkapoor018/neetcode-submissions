class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            best = 1

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    best = max(best, 1 + dfs(nr, nc))

            memo[(r, c)] = best
            return best
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res