class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return memo[i]
        
        return dfs(0)