class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The key idea is:
        # 1. Sort the array
        # 2. Fix one number
        # 3. Use two pointers to find the other two numbers
        nums.sort()

        result = set()

        for i in range(len(nums) - 2):

            j, k = i + 1, len(nums) - 1

            while j < k:

                currentSum = nums[i] + nums[j] + nums[k]

                if currentSum == 0:

                    result.add((nums[i], nums[j], nums[k]))

                    j += 1

                    k -= 1

                elif currentSum < 0:

                    j += 1

                else:

                    k -= 1

        return [list(t) for t in result]