class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
            dfs(i+1)

        dfs(0)#kickoff the decisions
        return res