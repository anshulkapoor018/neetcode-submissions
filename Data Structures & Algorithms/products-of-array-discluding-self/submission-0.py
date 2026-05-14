class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #default valus

        prefix = 1
        pre = []
        post = []

        # loop from left
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        # loop from right
        for i in range(len(nums) - 1 , -1, -1):
            res[i] *= postfix # multiplying the postfix with previous prefix values in last pass
            postfix *= nums[i]
            

        return res