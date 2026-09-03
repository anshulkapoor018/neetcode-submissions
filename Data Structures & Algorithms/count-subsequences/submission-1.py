class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # bottom up
        #bottom up
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m + 1)]

        for i in range(m+1):
            dp[i][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    useChar = dp[i+1][j+1]
                    skipChar = dp[i+1][j]
                    dp[i][j] = useChar + skipChar
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]

        #top down
        memo = {}

        def dfs(i, j):
            if j == len(t): return 1

            if i == len(s): return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == t[j]:
                useChar = dfs(i+1, j+1)
                skipChar = dfs(i + 1, j)
                memo[(i, j)] = useChar + skipChar
            else:
                memo[(i, j)] = dfs(i+1, j)
            
            return memo[(i, j)]
        return dfs(0, 0)