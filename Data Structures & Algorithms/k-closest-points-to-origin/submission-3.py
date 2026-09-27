class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxH = []
        heapq.heapify(maxH)

        for p in points:
            x, y = p
            euclideanDist = x*x + y*y

            heapq.heappush(maxH, (-euclideanDist, x, y))
            
            if len(maxH) > k:
                heapq.heappop(maxH)
        
        return [(x, y) for dist, x, y in maxH]