class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in numset:
                l = 1
                while num + l in numset:
                    l += 1
                
                res = max(res, l)
        return res
                    