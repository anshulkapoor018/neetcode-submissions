class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return True
            if remaining < 0:
                return False
            if i == len(nums):
                return False
            
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            take = dfs(i + 1, remaining - nums[i])
            skip = dfs(i + 1, remaining)

            memo[(i, remaining)] = take or skip

            return take or skip

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        return dfs(0, target)
        dfs(0, sum(nums))
