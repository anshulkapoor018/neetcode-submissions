class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return
            
            visited.add((r, c))

            # Explore neighboring cells that are
            # equal or higher in elevation
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        #start DFS from Pacific
        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c])

        # start DFSfrom Atlantic
        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, COLS-1, atlantic_reachable, heights[r][COLS-1])
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r, c])
        
        return res
