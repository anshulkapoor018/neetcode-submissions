class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        fresh = 0

        # add all rotten oranges to q and find fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        mins = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    
                    #out of bound check
                    if newR < 0 or newC < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] != 1:
                        continue
                    
                    # mark as rotten, reduce number of fresh
                    grid[newR][newC]=2
                    fresh -= 1

                    q.append((newR, newC)) # add to q of rotten
            mins += 1
        

        return mins if fresh == 0 else -1