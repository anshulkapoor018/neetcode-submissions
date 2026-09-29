class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] # start idx, height
        best = 0

        for i, h in enumerate(heights + [0]):
            start = i
            while st and st[-1][1] > h:
                idx, height = st.pop()
                best = max(best, height *(i - idx))
                start = idx
            st.append((start, h))

        return best