class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            firstMatch = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j+1] == '*':
                skip = dfs(i, j+2)
                useStar = firstMatch and dfs(i+1, j)
                memo[(i, j)] = skip or useStar
            else:
                memo[(i, j)] = firstMatch and dfs(i+1, j+1)

            return memo[(i, j)]
        return dfs(0, 0)