class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for c, pre in prerequisites:
            preMap[c].append(pre)
        
        visiting = set()
        visited = set()
        output = []

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            output.append(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output