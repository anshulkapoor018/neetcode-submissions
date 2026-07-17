class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            heaviest = -heapq.heappop(maxHeap) #heaviest
            secondHeaviest = -heapq.heappop(maxHeap) #second heaviest

            if secondHeaviest != heaviest:
                heaviest = heaviest - secondHeaviest
                heapq.heappush(maxHeap, -1 * heaviest)
        
        if not maxHeap:
            return 0
        
        return -maxHeap[0]
                