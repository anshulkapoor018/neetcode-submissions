class MedianFinder:
#     Store the lower half in a max-heap and the upper half in a min-heap.
# Insert into lower, move its maximum to upper, then rebalance by moving upper’s minimum back if needed.
# Return the lower root for odd size, or average both roots for even size.

    def __init__(self):
        self.lower = [] #max heap 
        self.upper = [] #min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2
        