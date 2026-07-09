class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]

            # Choice 1: decode one digit
            memo[i] = dfs(i + 1)

            # Choice 2: decode two digits if valid
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                memo[i] += dfs(i + 2)

            return memo[i]
        
        return dfs(0)
