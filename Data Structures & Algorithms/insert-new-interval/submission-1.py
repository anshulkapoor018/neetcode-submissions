class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            start, end = interval

            # current interval completely before newInterval
            if end < newInterval[0]:
                res.append(interval)
            # newInterval is completely before current interval
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # overlap
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        res.append(newInterval)

        return res
