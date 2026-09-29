class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True: # find intersection
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0] # reset to find entrance of cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
            