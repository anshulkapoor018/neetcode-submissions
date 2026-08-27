class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # build adjacency list: src -> list of destinations
        # sort tickets in reverse lexicographic order so that when we
        # later pop() from the end of each list, we get the
        # smallest destination first (pop() removes from the end, O(1))
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)  # reverse sort so pop() gives smallest

        route = []

        def dfs(airport):
            # keep consuming tickets out of this airport until none remain
            # (using while + pop() mutates the graph, so each ticket/edge
            # is used exactly once - this is Hierholzer's algorithm for
            # finding an Eulerian path)
            while graph[airport]:
                # always pop the lexicographically smallest unused
                # destination available from this airport
                dfs(graph[airport].pop())

            # post-order: only append this airport once we've fully
            # explored (used up) every ticket reachable from it -
            # this guarantees dead-ends get flushed out first
            route.append(airport)

        # start the itinerary from JFK, as required by the problem
        dfs("JFK")

        # route was built in post-order (dead-ends/leaves added first,
        # JFK added last), so reverse it to get the actual travel order
        return route[::-1]