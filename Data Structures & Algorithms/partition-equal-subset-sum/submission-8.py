class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        
        for n in nums:
            for t in range(target, n - 1, -1):
                dp[t] = dp[t] or dp[t-n]

        return dp[target]