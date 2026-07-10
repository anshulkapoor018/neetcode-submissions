class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i, remaining):
            # Successfully formed the target sum
            if remaining == 0:
                return True

            # Invalid path
            if remaining < 0 or i == len(nums):
                return False

            # Reuse solved state
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Choose to take or skip the current number
            take = dfs(i + 1, remaining - nums[i])
            skip = dfs(i + 1, remaining)

            memo[(i, remaining)] = take or skip
            return memo[(i, remaining)]

        total = sum(nums)

        # Odd total can never be split equally
        if total % 2 != 0:
            return False

        target = total // 2

        return dfs(0, target)