class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):                
                substr = s[start : end + 1]
                if isPalindrome(substr):
                    path.append(substr)
                    backtrack(end + 1)
                    path.pop()
        
        def isPalindrome(s: str) -> bool:
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

        backtrack(0)
        return res