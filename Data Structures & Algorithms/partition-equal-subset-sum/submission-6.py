class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2

        def dfs(i, target):
            if target == 0:
                return True
            
            if i == len(nums) or target < 0:
                return False
                
            if (i, target) in memo:
                return memo[(i, target)]
            
            skip = dfs(i+1, target)
            take = dfs(i+1, target - nums[i])

            memo[(i, target)] = skip or take

            return memo[(i, target)]
        
        return dfs(0, target)