class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return

            # mark as visited 
            board[r][c] = "S"

            #explore all directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        #kickoff DFS from COLS
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        #kickoff DFS from ROWS
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X" #capture it
                elif board[r][c] == "S":
                    board[r][c] = "O" #revert to O
                    