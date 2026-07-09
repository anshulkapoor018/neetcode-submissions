class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""

        def expand(left, right):
            nonlocal best
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Update longest palindrome found so far
                if len(s[left:right + 1]) > len(best):
                    best = s[left:right + 1]

                left -= 1

                right += 1

        # Try every possible center

        for i in range(len(s)):

            expand(i, i)       # Odd-length palindrome

            expand(i, i + 1)   # Even-length palindrome

        return best