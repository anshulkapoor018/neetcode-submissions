class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""  # longest palindromic substring found so far

        def expand(l, r):
            nonlocal best
            # grow outward from center (l, r) as long as we're in bounds
            # and both sides still mirror each other
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # this expansion is valid - check if it's our new longest palindrome
                if len(s[l:r + 1]) > len(best):
                    best = s[l:r + 1]

                # push both pointers one step further outward and try again
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)      # treat i as the center of an odd-length palindrome
            expand(i, i + 1)  # treat the gap between i and i+1 as the center of an even-length palindrome

        return best