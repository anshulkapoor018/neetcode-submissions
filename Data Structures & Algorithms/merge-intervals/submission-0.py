class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []

        for start, end in intervals:
            # If res is empty OR current interval starts after previous merged interval ends,
            # there is no overlap, so start a new merged interval.
            if not res or start > res[-1][1]:
                res.append([start, end])
            else: 
                #overlap, just change the end of last merged interval
                res[-1][1] = max(res[-1][1], end)
        
        return res