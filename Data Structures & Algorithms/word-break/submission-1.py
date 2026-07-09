class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # dp[i] = whether s[i:] can be segmented
        dp = [False] * (n + 1)

        # Empty suffix is successfully segmented
        dp[n] = True

        # Build from right to left because dp[i] depends on future indices
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                # If word matches here, trust the remaining suffix result
                if s.startswith(word, i):
                    dp[i] = dp[i + len(word)]

                    # One valid split is enough
                    if dp[i]:
                        break

        return dp[0]
        # -------------------------- 
        
        # memo = {}

        # def dfs(i):
        #     # Successfully segmented the entire string
        #     if i == len(s):
        #         return True

        #     # Reuse previously solved suffix
        #     if i in memo:
        #         return memo[i]

        #     # Try every dictionary word at the current position
        #     for word in wordDict:
        #         if s.startswith(word, i):
        #             if dfs(i + len(word)):
        #                 memo[i] = True
        #                 return True

        #     # No valid segmentation from this index
        #     memo[i] = False
        #     return False

        # return dfs(0)