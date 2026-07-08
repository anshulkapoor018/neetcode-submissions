class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list:
        # node -> [(neighbor, travel_time)]
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # Min heap stores (current_time, current_node)
        # Start from source node k with time = 0
        minHeap = [(0, k)]

        # Nodes whose shortest distance has been finalized
        visit = set()

        # Tracks the longest shortest-path seen so far
        t = 0

        while minHeap:
            # Get the node reachable in the least amount of time
            w1, n1 = heapq.heappop(minHeap)

            # Already processed with the shortest distance
            if n1 in visit:
                continue

            # Finalize shortest distance for this node
            visit.add(n1)

            # The answer is the maximum shortest-path distance
            t = max(t, w1)

            # Relax all outgoing edges
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # If every node was reached, return the last arrival time.
        # Otherwise, some node is unreachable.
        return t if len(visit) == n else -1