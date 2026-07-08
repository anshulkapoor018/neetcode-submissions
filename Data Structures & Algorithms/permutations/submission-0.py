class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def dfs(): 
            #base case
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue
                
                path.append(num)
                used.add(num)

                dfs()

                path.pop()
                used.remove(num)

        dfs()
        return res