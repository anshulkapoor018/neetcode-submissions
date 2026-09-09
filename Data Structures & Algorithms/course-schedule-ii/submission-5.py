class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological
        preMap = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for c, pre in prerequisites:
            preMap[pre].append(c)
            indegree[c] += 1
        
        q = deque()

        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        output = []

        while q:
            c = q.popleft()
            output.append(c)

            for nei in preMap[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return output if len(output) == numCourses else []
