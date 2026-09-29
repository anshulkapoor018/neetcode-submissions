class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up
        n = len(s)
        dp = [False] * (n+1)

        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if s.startswith(word, i):
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        
        return dp[0]

        # top down
        # memo = {}

        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     if i in memo:
        #         return memo[i]
            
        #     for word in wordDict:
        #         if s.startswith(word, i):
        #             if dfs(i + len(word)):
        #                 memo[i] = True
        #                 return True
        #     memo[i] = False
        #     return False
        
        # return dfs(0)