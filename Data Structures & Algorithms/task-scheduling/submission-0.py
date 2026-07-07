class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxH = [-cnt for cnt in count.values()]
        heapq.heapify(maxH)

        time = 0
        q = deque() #pair of [-cnt, idleTime] 

        while maxH or q:
            time +=1
            if maxH:
                cnt = 1 + heapq.heappop(maxH) # process
                if cnt:
                    q.append([cnt, time+n]) # add to q for processing later
            
            if q and q[0][1] == time:
                heapq.heappush(maxH, q.popleft()[0])
                
        
        return time