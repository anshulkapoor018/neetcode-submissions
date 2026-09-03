class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #bottom up
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m + 1)]

        for i in range(m+1):
            dp[i][n] = m - i

        for j in range(n+1):
            dp[m][j] = n - j
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

        # top down
        # memo = {}

        # def dfs(i, j):
        #     if i == len(word1):
        #         return len(word2) - j
            
        #     if j == len(word2):
        #         return len(word1) - i

        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     if word1[i] == word2[j]:
        #         memo[(i, j)] = dfs(i+1, j+1)
        #     else:
        #         replace = 1 + dfs(i+1, j+1)
        #         delete = 1 + dfs(i+1, j)
        #         insert = 1 + dfs(i, j + 1)
        #         memo[(i, j)] = min(replace, delete, insert)
            
        #     return memo[(i, j)]
        
        # return dfs(0, 0)