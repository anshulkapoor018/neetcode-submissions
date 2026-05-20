class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize result with first element
        res = nums[0]

        # Binary search pointers
        l, r = 0, len(nums) - 1

        while l <= r:

            # If current subarray is already sorted,
            # then leftmost element is the minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # Find middle index
            m = l + (r - l) // 2

            # Update minimum candidate
            res = min(res, nums[m])

            # If middle element belongs to left sorted portion,
            # minimum must be on the right side
            if nums[m] >= nums[l]:
                l = m + 1

            # Otherwise minimum is in left half
            else:
                r = m - 1

        return res