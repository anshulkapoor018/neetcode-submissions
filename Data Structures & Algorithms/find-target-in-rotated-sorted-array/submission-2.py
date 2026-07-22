class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if target == nums[mid]:
                return mid
            
            #left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    # we shift r now to shrink
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right hald is sorted
                if nums[mid] < target <= nums[r]:
                    # we shift l now to shrink
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1