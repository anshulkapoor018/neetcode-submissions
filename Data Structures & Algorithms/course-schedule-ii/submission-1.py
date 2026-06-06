class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if cycle present, we cant finish courses, 
        # so we need to deduce that, along with order
        order = []
        #building adjacency list
        preMap = {i : [] for i in range(numCourses)}

        for c, pre in prerequisites:
            preMap[c].append(pre)
        
        visiting = set()
        visited = set()

        def dfs(course):
            #cycle detected
            if course in visiting:
                return False

            if course in visited:
                return True
            
            visiting.add(course) # add current node/course

            # explore all paths
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course) # remove since paths explored
            visited.add(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order