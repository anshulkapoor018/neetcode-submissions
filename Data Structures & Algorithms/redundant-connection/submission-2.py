class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find(x)    → tells us the representative/root of x's group
        # union(a,b) → merges two groups
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_b] = root_a
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
