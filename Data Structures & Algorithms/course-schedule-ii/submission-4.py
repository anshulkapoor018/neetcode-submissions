class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i: [] for i in range(numCourses) }

        for c, pre in prerequisites:
            preMap[c].append(pre)
        
        visiting = set()
        visited = set()
        output = []

        def dfs(c):
            if c in visiting:
                return False #cycle

            if c in visited:
                return True
            
            visiting.add(c)

            for nei in preMap[c]:
                if not dfs(nei):
                    return False

            visiting.remove(c)
            visited.add(c)
            output.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output