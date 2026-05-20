class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search pointers
        l, r = 0, len(nums) - 1

        while l <= r:

            # Find middle index
            m = l + (r - l) // 2

            # Target found
            if nums[m] == target:
                return m

            # -----------------------------------
            # Check if LEFT half is sorted
            # -----------------------------------
            if nums[l] <= nums[m]:

                # Target lies inside left sorted half
                if nums[l] <= target < nums[m]:
                    r = m - 1

                # Otherwise search right half
                else:
                    l = m + 1

            # -----------------------------------
            # Otherwise RIGHT half is sorted
            # -----------------------------------
            else:

                # Target lies inside right sorted half
                if nums[m] < target <= nums[r]:
                    l = m + 1

                # Otherwise search left half
                else:
                    r = m - 1

        # Target not found
        return -1