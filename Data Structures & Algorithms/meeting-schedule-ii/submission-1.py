"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        # intervals.sort(key=lambda interval: interval.start)
        # Sort all start times and end times independently
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        s, e = 0, 0
        rooms, maxRooms = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                rooms += 1
                maxRooms = max(rooms, maxRooms)
                s += 1
            else: 
                #free a room
                rooms -= 1
                e += 1

        return maxRooms