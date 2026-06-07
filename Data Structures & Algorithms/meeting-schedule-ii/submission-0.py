"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intuition is At any moment, what is the maximum number of overlapping meetings?
        # maximum overlap is actually minimum rooms needed

        intervals.sort(key=lambda interval: interval.start)

        rooms = [] # min heap helps store end times of meetings

        for i in intervals:
            if rooms and rooms[0] <= i.start:
                #reuse the room
                heapq.heappop(rooms)

            #now add current meetings end time to heap to occupy the room
            heapq.heappush(rooms, i.end)
            
        return len(rooms)