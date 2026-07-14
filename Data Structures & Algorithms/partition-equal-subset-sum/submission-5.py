class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        possible = {0}
        target = total // 2

        for num in nums:
            new_possible = set(possible)

            for curr_sum in possible:
                new_possible.add(curr_sum + num)

            possible = new_possible

            if target in possible:
                return True

        return False

        # memo = {}

        # def dfs(i, target):
        #     # choices: skip nums[i], take nums[i]
        #     if target == 0:
        #         return True
            
        #     if i == len(nums) or target < 0:
        #         return False
            
        #     if (i, target) in memo:
        #         return memo[(i, target)]

        #     skip = dfs(i + 1, target)
        #     take = dfs(i + 1, target - nums[i])

        #     memo[(i, target)] = skip or take
        #     return memo[(i, target)]
        # target = total // 2
        # return dfs(0, target)