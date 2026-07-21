class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = [] # (interval_size, interval_end)

        res = {}
        i = 0

        for q in sorted(queries):
            # Add intervals where start <= q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(minHeap, (size, end))
                i += 1

            # Remove intervals where end < q
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # heap[0] gives smallest valid interval
            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1
        
        return [res[q] for q in queries]