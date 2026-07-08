class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(currentString, openCount, closeCount):
            if len(currentString) == 2 * n:
                res.append(currentString)
                return
            
            if openCount < n:
                backtrack(currentString + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                backtrack(currentString + ")", openCount, closeCount + 1)
        backtrack("", 0, 0)
        return res