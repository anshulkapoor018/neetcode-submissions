class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # core intuition
        # 1. Duplicates are allowed across different recursion levels.
        # 2. Duplicates are skipped within the same recursion level.
        # 3. each index can be used at most once
        candidates.sort()
        res = []
        subset = []

        def dfs(start, total):
            if total == target:
                res.append(subset.copy())
                return

            if total > target:
                return
            
            for i in range(start, len(candidates)):
                #skipping duplicates
                if i > start and candidates[i] == candidates[i-1]: 
                    continue
                
                subset.append(candidates[i])

                dfs(i+1, total+candidates[i])

                subset.pop()

        dfs(0, 0)
        return res