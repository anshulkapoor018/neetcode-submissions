class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        needCount = Counter(t)
        have = {}
        required = len(needCount)   # number of unique chars we need satisfied
        formed = 0                  # number of unique chars currently satisfied

        l = 0
        res = ""
        resLen = float("inf")

        for r in range(len(s)):
            c = s[r]
            have[c] = have.get(c, 0) + 1

            if c in needCount and have[c] == needCount[c]:
                formed += 1

            # Shrink while the window is valid
            while formed == required:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]

                leftChar = s[l]
                have[leftChar] -= 1
                if leftChar in needCount and have[leftChar] < needCount[leftChar]:
                    formed -= 1

                l += 1

        return res