from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        l = 0
        maxLen = 0
        maxFreq = 0  # most frequent char count in current window

        for r in range(len(s)):
            # Add right char into current window
            count[s[r]] += 1

            # Track the highest frequency char in this window
            maxFreq = max(maxFreq, count[s[r]])

            # Window is invalid if chars to replace > k
            # replacements needed = window size - most frequent char count
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            # Current window is valid
            maxLen = max(maxLen, r - l + 1)

        return maxLen