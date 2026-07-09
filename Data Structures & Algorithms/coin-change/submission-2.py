class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            print(a)
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]


        # top Down
        # memo = {}

        # def dfs(remainingAmount):
        #     # Exact amount formed, no more coins needed
        #     if remainingAmount == 0:
        #         return 0

        #     # Overshot amount, invalid path
        #     if remainingAmount < 0:
        #         return float("inf")

        #     # Reuse solved subproblem
        #     if remainingAmount in memo:
        #         return memo[remainingAmount]

        #     best = float("inf")

        #     # Try choosing every coin
        #     for coin in coins:
        #         best = min(best, 1 + dfs(remainingAmount - coin))

        #     memo[remainingAmount] = best
        #     return best

        # ans = dfs(amount)

        # return -1 if ans == float("inf") else ans