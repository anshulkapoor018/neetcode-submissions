class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numSet:
                #start of a sequence
                l = 1
                while num + l in numSet:
                    l += 1
                res = max(res, l)
        
        return res