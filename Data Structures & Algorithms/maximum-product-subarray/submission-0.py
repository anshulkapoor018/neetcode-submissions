class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]

        curMin = nums[0]

        res = nums[0]

        for num in nums[1:]:

            tempMax = max(num, num * curMax, num * curMin)

            tempMin = min(num, num * curMax, num * curMin)

            curMax = tempMax

            curMin = tempMin

            res = max(res, curMax)

        return res