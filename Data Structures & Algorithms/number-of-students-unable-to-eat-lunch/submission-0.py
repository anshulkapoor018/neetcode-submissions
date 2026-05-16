class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # top sandwich index i = 0
        # if no student wansts sandwiches[0], return length of students

        n = len(students)
        q = deque(students)
        res = n

        for s in sandwiches:
            cnt = 0
            while cnt < n and q[0] != s:
                #removing student from front and sending to the back
                cur = q.popleft() 
                q.append(cur)   
                cnt += 1
            
            if q[0] == s: #got a sandwich they want
                q.popleft()
                res -= 1
            else:
                break
        
        return res