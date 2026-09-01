class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] = number of distinct combinations that sum to amount `a`
        dp = [0] * (amount + 1)
        dp[0] = 1  # exactly one way to make 0: use no coins

        # outer loop over coins (not amounts!) — this is what enforces
        # "combinations" rather than "permutations": each coin is fully
        # considered (in every possible quantity) before moving to the next,
        # so a given multiset of coins is only ever built in one fixed order
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]  # add ways that use at least one more of coin c

        return dp[amount]
        