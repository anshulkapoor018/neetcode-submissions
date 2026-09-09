class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # crucial insight: thinking "last" instead of "first" makes the neighbors at burst-time fully determined and independent of order
        nums = [1] + nums + [1] # to handle boundary
        memo = {}

        def dfs(l, r):
            if l + 1 == r: # nothing to burst
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            best = 0

            for k in range(l+1, r):
                coins = nums[l] * nums[k] * nums[r]
                coins += dfs(l, k) + dfs(k, r)
                best = max(best, coins)
            
            memo[(l, r)] = best

            return best
        
        return dfs(0, len(nums) - 1)
        