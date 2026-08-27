class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)  # reverse sort so pop() gives smallest

        route = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)  # post-order

        dfs("JFK")
        return route[::-1]