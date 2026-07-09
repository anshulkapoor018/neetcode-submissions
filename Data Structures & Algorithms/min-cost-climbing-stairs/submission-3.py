class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Intuition is If I step on stair i, I must pay cost[i], then choose the cheaper future path.
        #more optimised
        # Base: from the top, there is 1 valid way
        n = len(cost)
        one = 0  # ways from i + 1
        two = 0  # ways from i + 2

        # Build answer from stair n-1 down to stair 0
        for i in range(n - 1, -1, -1):
            curr = cost[i] + min(one, two)
            two = one
            one = curr
        
        return min(one, two)
        # -------------------------- 

        # bottom up DP
        # n = len(cost)
        # dp = [0] * (n + 2)

        # # one solution we know for sure
        # dp[n] = 0

        # # backwards looping
        # for i in range(n-1, -1, -1):
        #     dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        # return min(dp[0], dp[1])

        # -------------------------- 

        # memo = {}

        # def dfs(i):
        #     if i >= len(cost): # we reached the top
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

        #     return memo[i]
        
        # #can start from either stair, whichever is less costly
        # return min(dfs(0), dfs(1))