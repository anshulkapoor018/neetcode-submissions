class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)
        cooldown = deque()
        time = 0

        while maxHeap or cooldown:
            time += 1
            
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1

                if freq != 0:
                    cooldown.append((freq, time + n))
            
            if cooldown and cooldown[0][1] == time:
                freq, _ = cooldown.popleft()
                heapq.heappush(maxHeap, freq)
        
        return time