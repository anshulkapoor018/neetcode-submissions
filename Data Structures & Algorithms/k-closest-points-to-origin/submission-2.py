class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)

        for point in points:
            x1, y1 = point
            euclideanDistance = x1 * x1 + y1 * y1

            heapq.heappush(maxHeap, (-euclideanDistance, x1, y1))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [(x, y) for neg_dist, x, y in maxHeap]
