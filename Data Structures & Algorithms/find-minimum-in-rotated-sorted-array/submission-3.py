class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r-l) // 2

            # if mid is greater, than min is in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
