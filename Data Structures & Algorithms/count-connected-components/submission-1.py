class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
            
        components = 0

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        
        return components