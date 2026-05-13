class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # sum -> index

        for i, n in enumerate(nums):
            print(i, n)
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i