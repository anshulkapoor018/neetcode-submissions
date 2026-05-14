from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Result array initialized with 1s
        res = [1] * len(nums)

        # Build prefix products
        # res[i] contains product of everything LEFT of i
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Multiply postfix products
        # postfix contains product of everything RIGHT of i
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res