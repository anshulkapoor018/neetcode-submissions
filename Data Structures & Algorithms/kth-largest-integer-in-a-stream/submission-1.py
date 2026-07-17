class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.minHeap = nums


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
