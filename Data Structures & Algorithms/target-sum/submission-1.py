class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        total = sum(nums)

        if abs(target) > total or (target + total) % 2 != 0:
            return 0
        
        subsetTarget = (target + total) // 2

        def dfs(i, rem):
            if i == len(nums):
                return 1 if rem == 0 else 0
            
            if (i, rem) in memo:
                return memo[(i, rem)]
            
            skip = dfs(i + 1, rem)

            take = dfs(i + 1, rem - nums[i]) if rem - nums[i] >= 0 else 0

            memo[(i, rem)] = skip + take

            return memo[(i, rem)]
        
        return dfs(0, subsetTarget)