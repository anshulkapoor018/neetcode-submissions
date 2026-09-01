class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down
        memo = {}

        def dfs(i, remainingAmt):
            if remainingAmt == 0:
                return 1
            
            if remainingAmt < 0 or i == len(coins):
                return 0
            
            if (i, remainingAmt) in memo:
                return memo[(i, remainingAmt)]
            
            # two choices at each step, using coins[i]:
            #   1) skip coins[i] entirely, move on to the next coin type
            #   2) use one more coins[i] (stay at index i, since coins are unlimited)
            skip = dfs(i + 1, remainingAmt)
            take = dfs(i, remainingAmt - coins[i])

            memo[(i, remainingAmt)] = skip + take
            return memo[(i, remainingAmt)]

        return dfs(0, amount)