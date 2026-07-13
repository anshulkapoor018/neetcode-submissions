class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        used = set()
        res = []

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                used.add(num)
                path.append(num)

                dfs()

                path.pop()
                used.remove(num)

        dfs()
        return res