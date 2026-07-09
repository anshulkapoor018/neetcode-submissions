class Solution:
    def rob(self, nums: List[int]) -> int:

        # -------------------------- 

        # bottom up DP
        n = len(nums)
        dp = [0] * (n+2)

        # one solution we know for sure
        dp[n] = 0

        # backwards looping
        for i in range(n-1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
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