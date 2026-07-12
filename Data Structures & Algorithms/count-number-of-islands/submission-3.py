class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0" # sink the islan/mark as visited

            # Explore 4-directionally adjacent pixels
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    numOfIslands += 1
                    dfs(r, c)

        return numOfIslands
