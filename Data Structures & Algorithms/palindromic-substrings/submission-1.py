class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(l, r):
            nonlocal count
            # grow outward from center (l, r) as long as we're in bounds
            # and both sides still mirror each other
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1

                # push both pointers one step further outward and try again
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)      # treat i as the center of an odd-length palindrome
            expand(i, i + 1)  # treat the gap between i and i+1 as the center of an even-length palindrome

        return count