class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) # sort by starting times
        prevEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if prevEnd <= start: # no overlap, we update prevEnd
                prevEnd = end
            else: #overlap found
                res += 1
                prevEnd = min(prevEnd, end)
        
        return res
