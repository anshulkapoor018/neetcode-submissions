class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i -> pointer for string s (the subsequence we're looking for)
        # j -> pointer for string t (the larger string)
        i, j = 0, 0

        # Keep scanning until we reach the end of either string
        while i < len(s) and j < len(t):

            # If characters match, we've found the next character
            # of the subsequence, so move i forward
            if s[i] == t[j]:
                i += 1

            # Always move through t
            j += 1

        # If i reached the end of s, every character in s
        # was found in order inside t
        return i == len(s)