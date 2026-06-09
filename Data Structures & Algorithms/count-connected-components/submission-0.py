class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        components = 0

        def dfs(node):
            #we mark a node as visited
            visited.add(node)

            # Visit all connected neighbors
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for node in range(n):
            if node not in visited:
                # New unvisited node means new component
                components += 1
                dfs(node)
                
        return components