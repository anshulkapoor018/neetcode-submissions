class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears.
        count = Counter(tasks)

        # Max heap of remaining task frequencies.
        # Python uses a min heap, so store negative counts.
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        # Cooldown queue stores:
        # (remaining_count, time_when_task_can_run_again)
        cooldown = deque()

        time = 0

        while maxHeap or cooldown:
            time += 1

            # Execute the currently most frequent available task.
            if maxHeap:
                freq = heapq.heappop(maxHeap)

                # Since freq is negative, adding 1 reduces remaining count.
                freq += 1

                # If this task still has remaining executions,
                # place it into cooldown.
                if freq != 0:
                    cooldown.append((freq, time + n))

            # Move cooled-down task back into the heap
            # once it becomes available again.
            if cooldown and cooldown[0][1] == time:
                freq, _ = cooldown.popleft()
                heapq.heappush(maxHeap, freq)

        return time