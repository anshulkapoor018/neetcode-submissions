class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0
        
        for n in nums:
            if n - 1 not in numSet:
                l = 1
                while n + l in numSet:
                    l += 1
                
                count = max(count, l)
                    
        return count