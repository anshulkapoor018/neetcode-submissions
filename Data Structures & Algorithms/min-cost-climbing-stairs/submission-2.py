class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Intuition is If I step on stair i, I must pay cost[i], then choose the cheaper future path.
        memo = {}

        def dfs(i):
            if i >= len(cost): # we reached the top
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]
        
        #can start from either stair, whichever is less costly
        return min(dfs(0), dfs(1))