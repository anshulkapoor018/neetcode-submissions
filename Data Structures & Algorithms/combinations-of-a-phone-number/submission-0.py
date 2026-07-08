class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []

        def backtrack(i, currentStr):
            if i == len(digits):
                res.append(currentStr)
                return
            
            digit = digits[i]
            letters = mapping[digit]

            for l in letters:
                backtrack(i + 1, currentStr + l)
        
        backtrack(0, "")

        return res



