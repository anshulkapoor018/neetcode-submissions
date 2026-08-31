class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remainingAmt):
            if remainingAmt == 0:
                return 0
            
            if remainingAmt < 0:
                return float("inf")
            
            if remainingAmt in memo:
                return memo[remainingAmt]
            
            best = float("inf")
            
            for c in coins:
                best = min(best, 1 + dfs(remainingAmt - c))
            
            memo[remainingAmt] = best

            return memo[remainingAmt]
            
        
        ans = dfs(amount)
        
        if ans == float("inf"):
            return -1
        else:
            return ans
        