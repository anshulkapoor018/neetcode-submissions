class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Key intuition: when two intervals overlap, 
        # remove the one with the larger end time, 
        # because the interval that ends earlier 
        # leaves more room for future intervals.
        intervals.sort(key=lambda x: x[0])
        removals = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >=prevEnd: #no overlap
                prevEnd = end
            
            else: #overlap
                removals += 1
                prevEnd = min(prevEnd, end)
        
        return removals