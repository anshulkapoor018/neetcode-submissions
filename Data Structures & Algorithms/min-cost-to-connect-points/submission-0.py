class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Prim's algorithm: grow MST from any starting point
        visited = set()
        minHeap = [(0, 0)]  # (cost_to_connect, point_index)
        totalCost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)

            # Skip points already added to MST
            if i in visited:
                continue

            # Add this point using the cheapest available edge
            visited.add(i)
            totalCost += cost

            x1, y1 = points[i]

            # Push edges from current point to all unvisited points
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, j))

        return totalCost