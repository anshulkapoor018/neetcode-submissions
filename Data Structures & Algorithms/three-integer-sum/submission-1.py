class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums) - 2):
             l = i + 1
             r = len(nums) - 1
             
             while l < r:
                currSum = nums[l] + nums[i] + nums[r]

                if currSum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif currSum > 0:
                    r -= 1
                else:
                    l += 1
            
        return [list(t) for t in res ]