class Solution:
    def rob(self, nums: List[int]) -> int:

        # -------------------------- 
        # bottom up DP
        n = len(nums)
        # dp[i] = max money we can rob starting from house i
        dp = [0] * (n + 2)

        # Build from the end because dp[i] depends on future houses
        for i in range(n - 1, -1, -1):
            rob_current = nums[i] + dp[i + 2]
            skip_current = dp[i + 1]
            dp[i] = max(rob_current, skip_current)

        return dp[0]

        # -------------------------- 
        
        # Recursion with memoization
        # memo = {}

        # def dfs(i):
        #     if i >= len(nums): # we reached the top
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

        #     return memo[i]
        
        # return dfs(0)