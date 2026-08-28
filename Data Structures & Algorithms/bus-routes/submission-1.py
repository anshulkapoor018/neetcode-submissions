class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # trivial case: already at the destination, no buses needed
        if source == target:
            return 0

        n = len(routes)

        # map: stop -> list of bus routes (indices) that pass through it
        # lets us find, for any stop, every bus we could board there
        stops = defaultdict(list)

        for bus in range(n):
            for stop in routes[bus]:
                stops[stop].append(bus)

        seenBus = set()            # buses we've already taken (no need to board again)
        seenStop = set([source])   # stops we've already reached
        res = 0                    # number of buses taken so far
        q = deque([source])        # BFS frontier of reachable stops

        while q:
            # process one full "level" = all stops reachable with `res` buses so far
            for _ in range(len(q)):
                stop = q.popleft()

                if stop == target:
                    return res  # reached destination - res is the bus count used

                # try boarding every bus that stops here
                for bus in stops[stop]:
                    if bus in seenBus:
                        continue  # already rode this bus on a previous stop, skip
                    seenBus.add(bus)

                    # riding this bus, every stop on its route becomes reachable
                    # with one more bus than the current level
                    for nxtStop in routes[bus]:
                        if nxtStop in seenStop:
                            continue  # already reached this stop some other way
                        seenStop.add(nxtStop)
                        q.append(nxtStop)

            # finished exploring all stops reachable with `res` buses;
            # everything newly queued required one additional bus ride
            res += 1

        # queue exhausted without ever reaching target - unreachable
        return -1