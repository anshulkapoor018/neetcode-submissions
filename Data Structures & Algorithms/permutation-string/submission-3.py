class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A permutation has the same character frequencies.
        # window size if fixed - len(s1)
        if len(s1) > len(s2):
            return False
        
        target = Counter(s1)
        window = {}
        l = 0

        for r in range(len(s2)):
            # add right char
            window[s2[r]] = window.get(s2[r], 0) + 1

            #if window is large, remove left char using 'l'
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]
                
                l += 1
            
            #compare only when window size == len(s1)
            if r - l + 1 == len(s1) and window == target:
                return True
        
        return False