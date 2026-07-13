class Solution:
    def isPalindrome(self, s: str) -> bool:
        actualS = ''.join(filter(str.isalnum, s))
        actualS = actualS.lower()
        start = 0 
        end = len(actualS) - 1

        while start <= end:
            if actualS[start] == actualS[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                piece = s[start:end + 1]

                if self.isPalindrome(piece):
                    path.append(piece)
                    dfs(end + 1)
                    path.pop()
        
        dfs(0)

        return res
        