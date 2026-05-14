class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        res = 0
        for i in nums:
            if i == 0:
                res = max(currentMax, res)
                currentMax = 0
            else:
                currentMax += 1
        
        return max(currentMax, res)
        
    
