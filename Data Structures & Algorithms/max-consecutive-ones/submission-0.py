class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        i = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] == 0: break
                cnt += 1
            currentMax = max(currentMax, cnt)

        
        return currentMax
        
    
