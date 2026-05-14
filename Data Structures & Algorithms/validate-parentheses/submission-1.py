class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        closedPar = { ")": "(", "}" : "{", ']': "["}

        for c in s:
            if c in closedPar:
                if res and res[-1] == closedPar[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)

        return True if not res else False