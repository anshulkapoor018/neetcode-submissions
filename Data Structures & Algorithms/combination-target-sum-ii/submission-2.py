class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(start, total):
            if total > target:
                return
            
            if total == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                subset.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                subset.pop()

        dfs(0, 0)
        return res
