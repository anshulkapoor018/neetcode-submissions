class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
            
            for n in nums:
                if n in used:
                    continue
                
                #decision 1
                used.add(n)
                path.append(n)

                dfs()

                #backtrack
                path.pop()
                used.remove(n)
                
        dfs()
        return res