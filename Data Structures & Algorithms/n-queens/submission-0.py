class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Queens attack format: 
        # same row
        # same column
        # same diagonal

        res = []
        board = [["."] * n for _ in range(n)] # create the board
        cols = set()

        #diagonals
        posDiag = set()  # r + c
        negDiag = set()  # r - c
        
        
        # Each row must contain exactly one queen. So at row r, our only decision is:
        # Which column should I place the queen in?
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                #place the Queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recurse to next
                dfs(r + 1)

                #remove the Queen
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        dfs(0)
        return res
