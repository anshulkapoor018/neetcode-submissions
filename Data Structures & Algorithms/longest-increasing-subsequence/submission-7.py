class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #bottom up
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(1+dp[j], dp[i])
        
        return max(dp)

        #top Down
        # memo = {}

        # def dfs(i, prev):
        #     if i == len(nums):
        #         return 0
            
        #     if (i, prev) in memo:
        #         return memo[(i, prev)]
            
        #     skip = dfs(i+1, prev)
        #     take = 0 

        #     if prev == -1 or nums[i] > nums[prev]:
        #         take = 1 + dfs(i + 1, i)
            
        #     memo[(i, prev)] = max(skip, take)
        
        #     return memo[(i, prev)]
        
        # return dfs(0, -1)