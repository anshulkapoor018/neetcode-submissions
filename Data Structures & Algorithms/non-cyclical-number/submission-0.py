class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set() #record visited sum of squares

        while n not in visit:
            visit.add(n)
            n = self.sumSquares(n)

            if n == 1:
                return True

        return False
        
    def sumSquares(self, n:int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        
        return output