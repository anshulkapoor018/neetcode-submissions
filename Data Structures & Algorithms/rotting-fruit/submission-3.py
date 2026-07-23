class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 = empty cell
        # 1 = fresh orange
        # 2 = rotten orange
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh:
            for _ in range(len(q)):
                currR, currC = q.popleft()

                for dr, dc in directions:
                    newR, newC = currR + dr, currC + dc

                    #check out of bounds
                    if newR < 0 or newC < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] != 1:
                        continue
                    
                    grid[newR][newC] = 2 #marking as rotten
                    fresh -= 1
                    q.append((newR, newC))
                
            minutes += 1
            
        if fresh == 0:
            return minutes
        else:
            return -1