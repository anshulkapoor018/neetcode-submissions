class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Case 1: newInterval comes before current interval
            # Since intervals are sorted, we can append it and return the rest
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: newInterval comes after current interval
            # No overlap, so keep current interval as is
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: intervals overlap
            # Merge current interval into newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # If newInterval belongs at the end, add it here
        res.append(newInterval)
        return res