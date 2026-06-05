class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # Convert nums into a min heap
        heapq.heapify(nums)

        # Keep only the k largest elements
        while len(nums) > k:
            heapq.heappop(nums)

        self.heap = nums

    def add(self, val: int) -> int:
        # Add new value
        heapq.heappush(self.heap, val)

        # Remove smallest if heap grows beyond k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Root is always kth largest
        return self.heap[0]