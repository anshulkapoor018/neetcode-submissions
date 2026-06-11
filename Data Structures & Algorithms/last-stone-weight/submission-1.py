import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Use negative values to simulate a max heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            # Largest stone
            y = -heapq.heappop(max_heap)

            # Second largest stone
            x = -heapq.heappop(max_heap)

            # If weights differ,
            # push the remaining stone back
            if y != x:
                heapq.heappush(max_heap, -(y - x))

        # No stones left
        if not max_heap:
            return 0

        # One stone left
        return -max_heap[0]