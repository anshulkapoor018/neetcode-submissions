class Solution:
    def trap(self, height: List[int]) -> int:
        # For any position i, how much water can sit above it?

        # It depends on:

        # tallest wall to the left
        # tallest wall to the right

        # The water level is limited by the shorter of those two walls.

        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]

        return water