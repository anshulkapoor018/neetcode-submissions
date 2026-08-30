class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up and space optimized
        # we dont care about previous states as we move along
        n = len(cost)
        one = 0 
        two = 0  
        
        # Build answer from stair n-1 down to stair 0
        for i in range(n-1, -1, -1):
            curr = cost[i] + min(one, two)
            two = one
            one = curr
        
        return min(one, two)

        #top down
        # memo = {}

        # def dfs(i):
        #     # base case
        #     if i >= len(cost): #reached the top
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))

        #     return memo[i]

        # return min(dfs(0), dfs(1))