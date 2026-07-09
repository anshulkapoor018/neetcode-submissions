class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up DP
        dp = [0] * (n + 2)

        # one solution we know for sure
        dp[n] = 1

        # backwards looping
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]

        # Recursion with memoization
        # memo = {}

        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = dfs(i + 1) + dfs(i + 2)

        #     return memo[i]
        
        # return dfs(0)