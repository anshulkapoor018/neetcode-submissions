class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        def expand(l, r):
            nonlocal best
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update longest palindrome found so far
                if len(s[l:r + 1]) > len(best):
                    best = s[l:r + 1]
                    
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)      # odd-length palindrome
            expand(i, i + 1)  # even-length palindrome
        
        return best
            