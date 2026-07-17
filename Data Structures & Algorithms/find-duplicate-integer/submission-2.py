class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Phase 1: find intersection inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # Phase 2: find entrance of cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


        
        # brute force
        # count = Counter(nums)

        # for k, v in count.items():
        #     if v > 1:
        #         return k