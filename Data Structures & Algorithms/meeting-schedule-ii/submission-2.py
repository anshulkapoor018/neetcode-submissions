"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        
        rooms = []

        for i in intervals:
            if rooms and rooms[0] <= i.start:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, i.end)
            
        return len(rooms)