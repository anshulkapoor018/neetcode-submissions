class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack storing:
        # (earliest_start_index, height)
        st = []
        maxArea = 0

        for i, h in enumerate(heights):
            # Current bar can initially start at its own index.
            start = i

            # If current bar is shorter, taller bars on the stack
            # can no longer extend to the right beyond index i - 1.
            while st and st[-1][1] > h:
                idx, height = st.pop()

                # Rectangle using this popped height spans
                # from idx up to i - 1.
                maxArea = max(maxArea, height * (i - idx))

                # Current shorter bar can extend back to the
                # earliest start index of the popped bar.
                start = idx

            # Push current height with the earliest index
            # from which it can form a valid rectangle.
            st.append((start, h))

        # Any bars still in the stack never found a shorter
        # bar to their right, so they can extend to the end.
        for i, h in st:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

        # brute Force
        # n = len(heights)
        # maxArea = 0

        # for i in range(n):
        #     h = heights[i]

        #     l = i
        #     r = i

        #     #Expand to left while bars are at least as tall
        #     while (l - 1) >= 0 and heights[l-1] >= h:
        #         l -= 1
            
        #     #Expand to right while bars are at least as tall
        #     while (r + 1) < n and heights[r + 1] >= h:
        #         r += 1
            
        #     width = r - l + 1
        #     maxArea = max(maxArea, h * width)
        
        # return maxArea
