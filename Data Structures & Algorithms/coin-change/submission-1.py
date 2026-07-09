class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remainingAmount):
            # Exact amount formed, no more coins needed
            if remainingAmount == 0:
                return 0

            # Overshot amount, invalid path
            if remainingAmount < 0:
                return float("inf")

            # Reuse solved subproblem
            if remainingAmount in memo:
                return memo[remainingAmount]

            best = float("inf")

            # Try choosing every coin
            for coin in coins:
                best = min(best, 1 + dfs(remainingAmount - coin))

            memo[remainingAmount] = best
            return best

        ans = dfs(amount)

        return -1 if ans == float("inf") else ans