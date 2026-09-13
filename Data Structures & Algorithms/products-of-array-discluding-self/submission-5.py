class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * len(nums)

        preFix = 1

        for i in range(n):
            res[i] = preFix
            preFix *= nums[i]

        postFix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= postFix
            postFix *= nums[i]
        
        return res