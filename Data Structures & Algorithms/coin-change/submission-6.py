class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up
        dp = [amount + 1] * (amount + 1) #minimum number of coins needed to make amount a
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        if dp[amount] >= amount + 1:
            return -1
        return dp[amount]
        # top down
        # memo = {}

        # def dfs(remainingAmount):
        #     if remainingAmount == 0 :
        #         return 0
            
        #     if remainingAmount < 0:
        #         return float("inf")
            
        #     if remainingAmount in memo:
        #         return memo[remainingAmount]
            
        #     best = float("inf")

        #     for c in coins:
        #         best = min(best, 1 + dfs(remainingAmount - c))
            
        #     memo[remainingAmount] = best
        #     return best
        
        # ans = dfs(amount)

        # if ans == float("inf"):
        #     return -1
        # return ans