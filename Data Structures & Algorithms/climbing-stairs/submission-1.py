class Solution:
    def climbStairs(self, n: int) -> int:
        # every step choices : go 1 step, go 2 steps

        # cache stores already computed answers
        memo = {} ## memoize seen paths

        def dfs(i):
            # Reached exactly n steps -> valid way
            if i == n:
                return 1
            # Went beyond n -> invalid path
            if i > n:
                return 0

            # Return cached result
            if i in memo:
                return memo[i]

            # Try taking 1 step and 2 steps
            memo[i] = dfs(i + 1) + dfs(i + 2)

            return memo[i]

        return dfs(0)