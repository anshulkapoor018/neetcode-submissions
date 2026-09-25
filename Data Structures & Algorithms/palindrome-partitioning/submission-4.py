class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        currentPartition = []

        def isPalindrome(s):
            return s == s[::-1]
        
        def backtrack(i):
            if i == len(s):
                res.append(currentPartition.copy())
                return
            
            for end in range(i, len(s)):
                piece = s[i:end + 1]
                if isPalindrome(piece):
                    currentPartition.append(piece)
                    backtrack(end+1)
                    currentPartition.pop()
        backtrack(0)
        return res
                