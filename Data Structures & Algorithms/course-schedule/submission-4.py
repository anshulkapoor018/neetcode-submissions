class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # unvisited → we have not started exploring this course
        # visiting  → this course is currently in the active DFS path
        # visited   → this course has already been fully verified as safe

        pre_map = {i: [] for i in range(numCourses)}

        for c, pre in prerequisites:
            pre_map[c].append(pre)
        
        visiting = set()
        
        def dfs(course):
            if course in visiting: # cycle detected
                return False

            if pre_map[course] == []:
                return True
            
            visiting.add(course) 
        
            for pre in pre_map[course]:
                if not dfs(pre):
                    visiting.remove(course)
                    return False
            
            visiting.remove(course)
            pre_map[course] = []
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True