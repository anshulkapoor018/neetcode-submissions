class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total): # at every step we make two decisions, include element, or not include
            #base case
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return
            #decision 1 take the element
            subset.append(nums[i])
            dfs(i, total + nums[i])

            #backtrack
            subset.pop()
            #decision 2 skip the element
            dfs(i+1, total)

        dfs(0, 0)#kickoff the decisions
        return res