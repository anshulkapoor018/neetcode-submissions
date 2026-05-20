class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right

        while left <= right:
            k = left + (right - left) // 2

            total_hours = 0
            for bananas in piles:
                total_hours += math.ceil(bananas / k)

            # Koko can finish within h hours
            if total_hours <= h:
                answer = k
                right = k - 1
            else:
                left = k + 1

        return answer