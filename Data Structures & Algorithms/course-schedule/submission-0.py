class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if cycle present, we cant finish courses, 
        # so we need to deduce that
        
        #building adjacency list
        preMap = {i : [] for i in range(numCourses)}

        for c, pre in prerequisites:
            preMap[c].append(pre)
        
        visiting = set()

        def dfs(course):
            #cycle detected
            if course in visiting:
                return False
            
            if preMap[course] == []:
                return True
            
            visiting.add(course) # add current node/course

            # explore all paths
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course) # remove since paths explored

            #memoize
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True