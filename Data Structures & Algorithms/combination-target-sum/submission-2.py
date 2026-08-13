class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # core intuition
        # 1. Include candidates[i]
        # 2. Skip candidates[i]
        res = []
        subset = []

        def dfs(i, total):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(subset.copy())
                return
            
            #decision 1 : include candidates[i]
            subset.append(nums[i])
            dfs(i, total + nums[i])

            #backtrack
            subset.pop()

            #decision 2 : exclude candidates[i]
            dfs(i + 1, total)

        dfs(0, 0)
        return res