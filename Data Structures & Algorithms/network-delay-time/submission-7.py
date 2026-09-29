class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algo
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t)) # u -> (v, w) [(neighbor, travel_time)]
        
        minH = [(0, k)] # (currentTime, currentNode)
        visit = set()
        time = 0

        while minH:
            t1, n1 = heapq.heappop(minH) # get node reachable fastest

            if n1 in visit: # already processed
                continue
            
            visit.add(n1)

            time = max(time, t1)

            for n2, t2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, (t1 + t2, n2))
        
        return time if len(visit) == n else -1

