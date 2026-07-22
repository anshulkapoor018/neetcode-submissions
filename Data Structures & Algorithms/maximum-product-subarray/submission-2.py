class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin = 1
        currMax = 1

        for n in nums:
            tmpMin = min(n, n * currMax, n * currMin)
            tmpMax = max(n, n * currMax, n * currMin)
            
            currMax = tmpMax
            currMin = tmpMin

            res = max(res, currMax)
        return res