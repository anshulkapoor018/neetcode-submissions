class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Prim's algorithm: grow MST from any starting point
        minHeap = [(0, 0)] # cost, pointIdx
        totalCost = 0
        visited = set()
        
        while len(visited) < n:
            cost, point = heapq.heappop(minHeap)
            
            if point in visited:
                continue
            
            visited.add(point)
            totalCost += cost

            x1, y1 = points[point]
            
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, j))
            
        return totalCost