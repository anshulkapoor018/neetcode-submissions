class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency list
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w)) # u -> (v, w)
            
        minHeap = [(0, k)] # current time, current node(signalFrom node)
        visit = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            time = max(time, w1)

            # now explore neighbors
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return time if len(visit) == n else -1  
            