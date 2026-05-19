class Solution:
    def merge(self, nums1: List[int], m: int,
                    nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Pointer for last position in nums1
        # where next largest element should go
        last = m + n - 1

        # Compare elements from back of both arrays
        # and place larger one at the end
        while m > 0 and n > 0:

            # If current element in nums1 is larger
            if nums1[m - 1] > nums2[n - 1]:

                # Place it at the current last position
                nums1[last] = nums1[m - 1]

                # Move nums1 pointer left
                m -= 1

            else:
                # Otherwise place nums2 element
                nums1[last] = nums2[n - 1]

                # Move nums2 pointer left
                n -= 1

            # Move final position pointer left
            last -= 1

        # If nums2 still has remaining elements,
        # copy them into nums1
        # No need to handle nums1 leftovers because
        # they are already in correct position
        while n > 0:
            nums1[last] = nums2[n - 1]

            n -= 1
            last -= 1