class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []

        for i, interval in enumerate(intervals):
            start, end = interval

            if not res or start > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
