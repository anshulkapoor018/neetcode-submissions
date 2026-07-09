class Solution:
    def numDecodings(self, s: str) -> int:

        # -------------------------- 
        # bottom up DP
        n = len(s)
        dp = [0] * (n + 1)

        # one solution we know for sure
        dp[n] = 1

        # backwards looping
        for i in range(n-1, -1, -1):
            # A standalone '0' is invalid
            if s[i] == "0":
                dp[i] = 0
                continue
                
            dp[i] = dp[i+1]
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]

        # -------------------------- 

        # Recursive Solution
        # memo = {}
        # def dfs(i):
        #     if i == len(s):
        #         return 1

        #     if s[i] == "0":
        #         return 0
            
        #     if i in memo:
        #         return memo[i]

        #     # Choice 1: decode one digit
        #     memo[i] = dfs(i + 1)

        #     # Choice 2: decode two digits if valid
        #     if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
        #         memo[i] += dfs(i + 2)

        #     return memo[i]
        
        # return dfs(0)
