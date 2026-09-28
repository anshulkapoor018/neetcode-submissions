class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #bottom up
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for t in range(target, n-1, -1):
                skip = dp[t]
                take = dp[t - n]
                dp[t] = skip or take
        
        return dp[target]
            
         

        #top Down

        # memo = {}

        # total = sum(nums)

        # if total % 2 == 1:
        #     return False
        
        # target = total // 2

        # def dfs(i, target):
        #     if target == 0:
        #         return True
            
        #     if i == len(nums) or target < 0:
        #         return False
            
        #     if (i, target) in memo:
        #         return memo[(i, target)]
            
        #     # skip
        #     skip = dfs(i+1, target)
        #     # take
        #     take = dfs(i+1, target-nums[i])

        #     memo[(i, target)] = skip or take

        #     return memo[(i, target)]
        
        # return dfs(0, target)
            