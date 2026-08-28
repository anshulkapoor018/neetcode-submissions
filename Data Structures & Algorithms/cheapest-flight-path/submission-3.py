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
        best = {}
        
        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return cost  # heap pops by cost, so first time we reach dst is cheapest

            # prune: if we've already reached this node with fewer or equal
            # stops, this path can't possibly do better - skip it
            if node in best and best[node] <= stops:
                continue
            best[node] = stops

            # can't take another flight if we've already used k stops
            if stops > k:
                continue

            for nei, edgeCost in graph[node]:
                heapq.heappush(minHeap, (cost + edgeCost, nei, stops + 1))

        return -1