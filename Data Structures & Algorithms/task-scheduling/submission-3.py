class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxH = [-freq for freq in count.values()]
        heapq.heapify(maxH)
        cooldown = deque()
        time = 0

        while maxH or cooldown:
            time+= 1

            if maxH:
                freq = heapq.heappop(maxH)
                freq += 1

                if freq != 0:
                    #append back to cooldown
                    cooldown.append((freq, time + n)) # append with remaining freq plus unlock time
                
            if cooldown and cooldown[0][1] == time:
                freq, _ = cooldown.popleft()
                heapq.heappush(maxH, freq)
                
                
        return time
        