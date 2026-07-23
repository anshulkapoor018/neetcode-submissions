class Solution:
    def numDecodings(self, s: str) -> int:
        # 2 choices - 1 digit or 2 digit decoding

        memo = {}
        
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]
            
            res = dfs(i+1) # choice 1
        
            #choice 2 only if condition true

            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                res += dfs(i + 2)
            
            memo[i] = res

            return memo[i]
        
        return dfs(0)