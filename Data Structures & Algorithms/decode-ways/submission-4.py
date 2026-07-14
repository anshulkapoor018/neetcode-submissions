class Solution:
    def numDecodings(self, s: str) -> int:

        # bottom up

        dp = [0 for _ in range(len(s) + 1)]
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

                if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]
        
        return dp[0]
    
        # memo = {}

        # def dfs(i):
        #     #choice is 
        #     # take 1 digit
        #     # take 2 digits
        #     if i == len(s):
        #         return 1
            
        #     if s[i] == "0":
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     res = dfs(i + 1)
            
        #     if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
        #         res += dfs(i + 2)
            
        #     memo[i] = res

        #     return res
        
        # return dfs(0)
        

        