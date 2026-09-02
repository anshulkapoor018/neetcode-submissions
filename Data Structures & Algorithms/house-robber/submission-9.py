class Solution:
    def rob(self, nums: List[int]) -> int:

        one = 0
        two = 0

        for i in range(len(nums) - 1,  -1, -1):
            curr = max(nums[i] + two, one)
            two = one
            one = curr
        
        return one

        # memo = {}

        # def dfs(i): # 2 choices, rob or skip
        #     if i >= len(nums):
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(dfs(i+2) + nums[i], dfs(i+1))

        #     return memo[i]
        
        # return dfs(0)