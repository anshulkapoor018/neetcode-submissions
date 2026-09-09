class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses) }

        for c, pre in prerequisites:
            preMap[c].append(pre)
        
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            
            if preMap[c] == []:
                return True
            
            visiting.add(c)

            for nei in preMap[c]:
                if not dfs(nei):
                    return False

            visiting.remove(c)
            preMap[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True