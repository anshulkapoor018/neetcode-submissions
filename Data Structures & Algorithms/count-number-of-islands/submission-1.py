class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c): #Boundary check -> Action -> Explore all paths
            # Out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            # water
            if grid[r][c] == "0":
                return
            
            #Action
            # mark land we are on as visited
            grid[r][c] = "0"

            # Explore 4-directionally adjacent pixels
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c) # Sink the full connected island
        
        return islands
            