class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at each index i, we track min product till now and max product till now

        res = max(nums)
        currMin = 1
        currMax = 1
        
        for n in nums:
            tempMin = min(n, n * currMin, n * currMax)
            tempMax = max(n, n * currMin, n * currMax)
            
            currMax = tempMax
            currMin = tempMin

            res = max(currMax, res)
        
        return res