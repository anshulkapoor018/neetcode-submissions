class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])

        og_color = image[sr][sc] # og color we are allowed to replace

        # Important edge case:
        # If new color is same as original, no work needed.
        # Without this, DFS can keep revisiting changed cells forever.
        if og_color == color:
            return image

        def dfs(r, c): #Boundary check -> Action -> Explore all paths
            # Out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            # Already visited in current path OR blocked cell
            if image[r][c] != og_color:
                return
            
            #Action
            # Repaint current cell
            image[r][c] = color

            # Explore 4-directionally adjacent pixels
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        
        dfs(sr, sc)
        return image

            