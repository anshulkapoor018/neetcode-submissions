class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
         # valid tree means non non connected nodes
         # no cycles
        if len(edges) != n-1:
            return False
        
        adj = {i: [] for i in range(n)}
        #build adj list
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False # cycle found

            visit.add(node)
            
            for nei in adj[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node): 
                    return False

            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visit) == n