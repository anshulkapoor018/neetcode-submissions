class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Maintain a monotonic decreasing deque of indices.
        res = []
        dq = deque()
        l = 0

        for r in range(len(nums)):
            # remove smaller value from back since they cant be maximum in a window size k

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            #remove index thats out of current window
            if dq[0] < l:
                dq.popleft()
            
            #we reached window size needed
            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
            

        return res
        
        
        
        
        
        
        
        
        
        
        # Brute Force
        # res = []
        
        # for i in range(len(nums) - k + 1):
        #     res.append(max(nums[i: i + k]))
        
        # return res