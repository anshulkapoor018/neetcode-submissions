class Solution:
    def distance(self, x1, y1):
        # Euclidean distance from origin
        return x1*x1 + y1*y1

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for p in points:
            dist = self.distance(p[0], p[1])
            heapq.heappush(max_heap, (-dist, p[0], p[1]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [(x, y) for neg_dist, x, y in max_heap]



