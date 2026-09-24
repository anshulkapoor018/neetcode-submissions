class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        best = 0 

        for i, h in enumerate(heights + [0]):
            start = i
            while st and st[-1][1] > h:
                oldStart, oldHeight = st.pop()
                best = max(best, oldHeight * (i - oldStart))
                start = oldStart
            
            if not st or st[-1][1] < h:
                st.append((start, h))
        
        return best