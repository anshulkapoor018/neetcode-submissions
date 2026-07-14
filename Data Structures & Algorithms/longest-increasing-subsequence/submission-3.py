class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prevIndex):
            if i == len(nums):
                return 0
            
            if (i, prevIndex) in memo:
                return memo[(i, prevIndex)]

            skip = dfs(i + 1, prevIndex)

            take = 0
            if prevIndex == -1 or nums[i] > nums[prevIndex]:
                take = 1 + dfs(i + 1, i)
            
            memo[(i, prevIndex)] = max(skip, take)
            return memo[(i, prevIndex)]

        return dfs(0, -1)