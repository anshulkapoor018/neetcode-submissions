class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s.startswith(word, i):
                    if dp[i + len(word)]:
                        dp[i] = True
                        break

        return dp[0]
        # memo = {}

        # def dfs(i):

        #     if i == len(s): return True
        #     if i in memo: return memo[i]
        #     for word in wordDict:
        #         if s.startswith(word, i):
        #             if dfs(i + len(word)):
        #                 memo[i] = True
        #                 return True

        #     memo[i] = False

        #     return False

        # return dfs(0)
