class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            start, end = interval

            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append(interval)
            else: #overlap
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        res.append(newInterval)
    
        return res