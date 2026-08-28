class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        one = 1  # ways from i + 1
        two = 0  # ways from i + 2
        
        for i in range(n-1, -1, -1):
            curr = one + two
            two = one
            one = curr
        
        return one
        

        #top down
        # memo = {}

        # def dfs(i):
        #     # base case
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0 # going overboard

        #     if i in memo:
        #         return memo[i]

        #     memo[i] = dfs(i + 1) + dfs(i+2)

        #     return memo[i]
        
        # return dfs(0)     