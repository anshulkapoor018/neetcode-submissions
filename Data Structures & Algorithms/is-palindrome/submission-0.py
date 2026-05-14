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
