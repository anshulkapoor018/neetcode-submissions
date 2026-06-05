from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Cannot start from a blocked cell
        if grid[0][0] == 1:
            return -1

        q = deque([(0, 0)])
        visit = {(0, 0)}

        # Path length starts at 1 because (0,0) counts
        path_len = 1

        # 8 possible directions
        directions = [
            (0, 1),   (0, -1),  # Left, Right
            (1, 0),   (-1, 0),  # Down, Up
            (1, 1),   (1, -1),  # Diagonals
            (-1, 1),  (-1, -1)
        ]

        while q:
            # Process one BFS level at a time
            for _ in range(len(q)):
                r, c = q.popleft()

                # First time reaching destination = shortest path
                if r == ROWS - 1 and c == COLS - 1:
                    return path_len

                # Explore all 8 neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Skip invalid positions
                    if (
                        nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                    ):
                        continue

                    visit.add((nr, nc))
                    q.append((nr, nc))

            # One BFS layer = one additional step
            path_len += 1

        # Destination was never reached
        return -1