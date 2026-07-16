class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            h = heights[i]

            l = i
            r = i

            #Expand to left while bars are at least as tall
            while (l - 1) >= 0 and heights[l-1] >= h:
                l -= 1
            
            #Expand to right while bars are at least as tall
            while (r + 1) < n and heights[r + 1] >= h:
                r += 1
            
            width = r - l + 1
            maxArea = max(maxArea, h * width)
        
        return maxArea
