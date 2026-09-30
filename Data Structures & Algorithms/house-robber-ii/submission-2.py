class Solution:
    def robHelper(self, nums: List[int]) -> bool:
        one = 0
        two = 0

        for i in range(len(nums) - 1, -1, -1):
            curr = max(nums[i] + two, one)
            two = one
            one = curr

        return one

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        #split
        setOfHouses1 = nums[:n-1]
        setOfHouses2 = nums[1:n]

        return max(self.robHelper(setOfHouses1), self.robHelper(setOfHouses2))