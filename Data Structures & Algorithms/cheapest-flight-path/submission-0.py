class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Build directed adjacency list: airport -> [(neighbor, price)]
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Min heap stores: (total_cost_so_far, current_airport, stops_used)
        minHeap = [(0, src, 0)]

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)

            # First time destination is popped, it is the cheapest valid route
            if node == dst:
                return cost

            # Cannot take more flights if stops limit is already used
            if stops > k:
                continue

            # Try all outgoing flights from current airport
            for nei, edgeCost in graph[node]:
                heapq.heappush(minHeap, (cost + edgeCost, nei, stops + 1))

        return -1