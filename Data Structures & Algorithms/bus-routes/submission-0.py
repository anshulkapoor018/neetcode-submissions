class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        n = len(routes)
        stops = defaultdict(list)

        for bus in range(n):
            for stop in routes[bus]:
                stops[stop].append(bus)
        
        seenBus = set()
        seenStop = set([source])
        res = 0
        q = deque([source])

        while q:
            for _ in range(len(q)):
                stop = q.popleft()
                if stop == target:
                    return res
                
                for bus in stops[stop]:
                    if bus in seenBus:
                        continue
                    seenBus.add(bus)

                    for nxtStop in routes[bus]:
                        if nxtStop in seenStop:
                            continue
                        seenStop.add(nxtStop)
                        q.append(nxtStop)
                
            res += 1
        
        return -1