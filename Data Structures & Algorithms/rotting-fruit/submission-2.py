class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 = empty cell
        # 1 = fresh orange
        # 2 = rotten orange
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c)) # we get rotten oranges 
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh:
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()
            
                for dr, dc in directions:
                    newR, newC = curr_r + dr, curr_c + dc

                    if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or grid[newR][newC] != 1:
                        continue
                    
                    grid[newR][newC] = 2 # marking as rotten
                    fresh -= 1

                    queue.append((newR, newC))

            minutes += 1
        
        if fresh == 0:
            return minutes
        else:
            return -1