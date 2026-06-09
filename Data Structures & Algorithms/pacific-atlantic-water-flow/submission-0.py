class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # Cells reachable from Pacific and Atlantic oceans
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # Stop if:
            # 1. Out of bounds
            # 2. Already visited
            # 3. Current height is lower than previous
            #    (water cannot flow uphill when traversing from ocean inward)
            if (
                (r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))

            # Explore neighboring cells that are
            # equal or higher in elevation
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from Pacific borders
        # (top row and left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])

            # Atlantic border (bottom row)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Start DFS from Pacific left border
        # and Atlantic right border
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Cells reachable from BOTH oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res