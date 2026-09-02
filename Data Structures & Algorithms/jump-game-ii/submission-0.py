class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(nums[i] + i, farthest)
            
            if i == currEnd:
                jumps += 1
                currEnd = farthest
        
        return jumps