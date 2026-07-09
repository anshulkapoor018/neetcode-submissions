class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up 1D
        n = len(nums)
        dp = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(1+dp[j], dp[i])

        return max(dp) 


        # recursive solution with memoize
        memo = {}
        def dfs(i, prev):
            # No elements left to consider
            if i == len(nums):
                return 0
            
            if (i, prev) in memo:
                return memo[(i, prev)]

            # Skip current element
            skip = dfs(i + 1, prev)

            # Take current element if it keeps the sequence increasing
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i + 1, i)

            memo[((i, prev))] = max(skip, take)
            return max(skip, take)

        return dfs(0, -1)
