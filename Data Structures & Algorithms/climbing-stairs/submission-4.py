class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up, space optimised
        one = 1
        two = 0

        for i in range(n-1, -1, -1):
            curr = one + two
            two = one
            one = curr
        
        return one
        # memo = {}

        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = dfs(i+1) + dfs(i+2)

        #     return memo[i]
        
        # return dfs(0)