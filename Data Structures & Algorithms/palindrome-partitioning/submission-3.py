class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1

        while start <= end:
            if s[start] == s[end]:
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
        