class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) # sort by start time
        res = []

        for i, interval in enumerate(intervals):
            start, end = interval

            if not res or start > res[-1][1]: # start is well after the end of previous entry, we just append
                res.append(interval)
            else: # there is an overlap
                res[-1][1] = max(res[-1][1], end)
        
        return res