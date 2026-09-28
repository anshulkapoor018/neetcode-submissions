class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adj list
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t)) # u > (v, w)
        
        minH = [(0, k)] # current time, current node from where we are sending the signal
        time = 0
        visit = set()
        
        while minH:
            currentTime, currentNode = heapq.heappop(minH)
            
            if currentNode in visit:
                continue 

            visit.add(currentNode)
            
            time = max(currentTime, time)

            # now we explore neighbors
            for nei, t1  in adj[currentNode]:
                if nei not in visit:
                    heapq.heappush(minH, (t1 + currentTime, nei))
        
        return time if len(visit) == n else -1
                
                