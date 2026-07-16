class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A permutation has the same character frequencies.
        # window size if fixed - len(s1)
        windowSize = len(s1)
        if windowSize > len(s2):
            return False
        
        target = Counter(s1)

        for i in range(len(s2) - windowSize + 1):
            currentWindow = s2[i : i + windowSize]

            if Counter(currentWindow) == target:
                return True
        
        return False