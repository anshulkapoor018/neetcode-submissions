class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, prev):
            #base case:
            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            skip = dfs(i + 1, prev)
            
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i+1, i)

            memo[(i, prev)] = max(skip, take)
            return memo[(i, prev)]
        
        return dfs(0, -1)