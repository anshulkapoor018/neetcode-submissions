class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at each i, track max product so far and min product so far
        res = max(nums)
        curMax = 1
        curMin = 1

        for n in nums:
            tmpMax = max(n, n * curMax, n * curMin)
            tmpMin = min(n, n * curMax, n * curMin)
            curMax = tmpMax
            curMin = tmpMin
            
            res = max(res, curMax)
        return res