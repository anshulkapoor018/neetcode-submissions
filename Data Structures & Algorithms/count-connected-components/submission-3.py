class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        numberOfConnectedComponents = 0

        def dfs(node):
            #base case, cycle
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                numberOfConnectedComponents += 1
        
        return numberOfConnectedComponents