class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        l = len(nums3)
        # print(nums3)
        if l % 2 == 0:
            # print(nums3[l // 2], nums3[(l // 2) - 1])
            return (nums3[l // 2] + nums3[(l // 2) - 1]) / 2
        else:
            # print(nums3[l // 2])
            return (nums3[l // 2])