class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            
            parent[rootB] = rootA

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]