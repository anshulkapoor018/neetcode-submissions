from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window_size = len(s1)

        if window_size > len(s2):
            return False

        target = Counter(s1)

        for i in range(len(s2) - window_size + 1):

            # Current substring of length len(s1)
            window = s2[i:i + window_size]

            if Counter(window) == target:
                return True

        return False