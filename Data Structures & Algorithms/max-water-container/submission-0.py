class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r = 0, len(h) - 1
        res = 0

        while l < r:
            area = min(h[l], h[r]) * (r - l) # min of heights * breadth
            res = max(res, area)
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
            
        return res