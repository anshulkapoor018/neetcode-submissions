class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i, n in enumerate(nums):
            idxs[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in idxs and idxs[diff] != i:
                return [i, idxs[diff]]
        
        return []

