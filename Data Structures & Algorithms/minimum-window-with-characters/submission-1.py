class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t) # how many each letter we need
        have = {} #how many each letter frame holds
        required = len(need) #number of distinct letters we must satisy
        formed = 0 # how many have we satisfied currently
        l = 0
        best = ""

        for r in range(len(s)):
            c = s[r] 
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                formed += 1 # satisfied one more char
            
            while formed == required: # frame valid, now we shrink to minimize
                if best == "" or (r-l+1 < len(best)):
                    best = s[l: r + 1]
                
                left = s[l]
                have[left] -= 1
                if left in need and have[left] < need[left]:
                    formed -= 1 # shrinking broke a letter
                
                l += 1
            
        return best