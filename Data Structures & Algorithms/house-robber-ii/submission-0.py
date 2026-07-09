class Solution:
    def robHelper(self, nums: List[int]) -> int:
        #more optimised
        # Base: from the top, there is 1 valid way
        n = len(nums)
        one = 0  # ways from i + 1
        two = 0  # ways from i + 2

        # Build answer from stair n-1 down to stair 0
        for i in range(n - 1, -1, -1):
            curr = max(nums[i] + two, one)
            two = one
            one = curr
        return one

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Only one house, no circular conflict
        if n == 1:
            return nums[0]
        excludeFirst = nums[1:n]
        excludeLast = nums[:n-1]
        return max(self.robHelper(excludeFirst), self.robHelper(excludeLast))