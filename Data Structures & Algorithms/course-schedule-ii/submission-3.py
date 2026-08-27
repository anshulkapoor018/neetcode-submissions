class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS Topological Sort
        preMap = {i: [] for i in range(numCourses)}

        indegree = [0] * numCourses

        #pre -> course
        for c, pre in prerequisites:
            preMap[pre].append(c)
            indegree[c] += 1
        
        q = deque()

        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        output = []

        while q:
            course = q.popleft()
            output.append(course)

            for nei in preMap[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return output if len(output) == numCourses else []
        