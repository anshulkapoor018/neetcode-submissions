class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def hoursNeeded(k):
            h = 0
            for pile in piles:
                h += math.ceil(pile/k)
            return h

        ans = r
        while l <= r:
            k = l + (r-l) // 2
            
            if hoursNeeded(k) <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
            
        return ans