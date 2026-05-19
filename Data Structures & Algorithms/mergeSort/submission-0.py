# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        # Start merge sort on entire array
        return self.mergeHelper(pairs, 0, len(pairs) - 1)
    

    def mergeHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:

        # Base case:
        # If subarray has 0 or 1 element, it's already sorted
        if e - s + 1 <= 1:
            return pairs

        # Find middle index
        m = (s + e) // 2

        # Recursively sort left half
        self.mergeHelper(pairs, s, m)

        # Recursively sort right half
        self.mergeHelper(pairs, m + 1, e)

        # Merge the two sorted halves
        self.merge(pairs, s, m, e)

        return pairs


    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> List[Pair]:

        # Create copies of left and right subarrays
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]

        # i -> pointer for left array
        # j -> pointer for right array
        # k -> pointer for original array
        i, j, k = 0, 0, s

        # Compare elements from both halves
        # and place smaller one into original array
        while i < len(L) and j < len(R):

            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        # Add remaining elements from left half
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Add remaining elements from right half
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1