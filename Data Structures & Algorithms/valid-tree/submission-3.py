class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = {i:[] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components == 1
                    
                