class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up
        one = 0
        two = 0
        for i in range(len(nums) - 1, -1, -1):
            curr = max(nums[i]+two, one)
            two = one
            one = curr
        
        return one
        # 2 choices, rob or skip
        # memo = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     if i in memo: 
        #         return memo[i]
            
        #     memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            
        #     return memo[i]
        
        # return dfs(0)
            