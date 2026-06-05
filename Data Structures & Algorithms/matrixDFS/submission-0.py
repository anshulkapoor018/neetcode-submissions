class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            # Out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            # Already visited in current path OR blocked cell
            if (r, c) in visit or grid[r][c] == 1:
                return 0

            # Reached destination
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            # Mark current cell as visited
            visit.add((r, c))

            # Explore all 4 directions
            count = (
                dfs(r + 1, c, visit) +  # Down
                dfs(r - 1, c, visit) +  # Up
                dfs(r, c + 1, visit) +  # Right
                dfs(r, c - 1, visit)    # Left
            )

            # Backtrack so other paths can use this cell
            visit.remove((r, c))

            return count

        return dfs(0, 0, set())