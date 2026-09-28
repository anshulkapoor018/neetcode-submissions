class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minH = [(0, 0)]
        totalCost = 0

        while len(visited) < n:
            cost, point = heapq.heappop(minH)

            if point in visited:
                continue
            
            visited.add(point)
            totalCost += cost
            x1, y1 = points[point]

            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x2-x1) + abs(y2-y1)
                    heapq.heappush(minH, (dist, j))
                    

        return totalCost
            