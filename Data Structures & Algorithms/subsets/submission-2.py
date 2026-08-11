class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # core intuition
        # Do we include this number?
        # Do we skip this number?
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # decision 1
            subset.append(nums[i])
            dfs(i + 1)

            #backtrack
            subset.pop()

            # decision 2
            dfs(i + 1)

        dfs(0)
        return res