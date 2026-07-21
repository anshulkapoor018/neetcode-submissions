"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            #check if there is a conflict
            if curr.start < prev.end:
                return False

        return True
