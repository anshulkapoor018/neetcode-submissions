class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if s.startswith(w, i):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return memo[i]
        
        return dfs(0)