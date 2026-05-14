class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Greatest element seen so far from the right
        max_right = -1

        # Traverse array from right to left
        for i in range(len(arr) - 1, -1, -1):

            # Store current value before overwriting it
            current = arr[i]

            # Replace current element with greatest value to its right
            arr[i] = max_right

            # Update max_right if current value is larger
            max_right = max(max_right, current)

        return arr