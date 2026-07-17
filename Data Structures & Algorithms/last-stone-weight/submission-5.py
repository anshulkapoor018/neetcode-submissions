class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            stone2 = -heapq.heappop(maxHeap)
            stone1 = -heapq.heappop(maxHeap)

            if stone1 != stone2:
                stone2 = stone2 - stone1
                heapq.heappush(maxHeap, -1 * stone2)
        
        if not maxHeap:
            return 0
        
        return -maxHeap[0]
                