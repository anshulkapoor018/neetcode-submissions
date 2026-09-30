class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = []

        for num in nums:
            heapq.heappush(minH, num)

            if len(minH) > k:
                heapq.heappop(minH)
        
        return minH[0]