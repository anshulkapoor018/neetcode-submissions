class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        # Multi-source BFS:
        # Start from all gates (0) simultaneously and expand outward.
        # This guarantees the first time we reach a room is its shortest
        # distance to any gate.

        ROWS, COLS = len(rooms), len(rooms[0])

        visit = set()
        q = deque()

        def addRoom(r, c):
            # Skip if:
            # - out of bounds
            # - already visited
            # - wall (-1)
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visit or
                rooms[r][c] == -1
            ):
                return

            visit.add((r, c))
            q.append([r, c])

        # Add all gates as BFS starting points
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0

        # Process one BFS level at a time
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                # Current BFS level represents distance from nearest gate
                rooms[r][c] = dist

                # Explore 4-directional neighbors
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            # Next level is one step farther from a gate
            dist += 1