class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i): # at every step we make two decisions, include element, or not include
            #base case
            if i == len(nums):
                res.append(subset.copy())
                return
            #decision 1
            subset.append(nums[i])
            dfs(i+1)

            #backtrack
            subset.pop()
            #decision 2
            #exclude all duplicate values on this level
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i+1)

        dfs(0)#kickoff the decisions
        return res