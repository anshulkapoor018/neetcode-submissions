class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(start, remaining): # at every step we make two decisions, include element, or not include
            #base case
            if remaining == 0:
                res.append(subset.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # skipping duplicates on same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])

                #backtrack now
                dfs(i+1, remaining - candidates[i])

                subset.pop()

        dfs(0, target)#kickoff the decisions
        return res