class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

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
