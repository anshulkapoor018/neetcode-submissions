class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        l = 0

        for r in range(len(nums)):
            
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop() #  1. Remove smaller values from the back

            dq.append(r)

            # 2. Remove indices that fall outside the current window
            if dq[0] < l:
                dq.popleft()

            # once window reaches size k, record the max
            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
        
        return res