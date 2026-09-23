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
            "9": "wxyz"
        }

        res = []

        def dfs(i, currentString):
            if i == len(digits):
                res.append(currentString)
                return
            
            digit = digits[i]
            letters = mapping[digit]

            for l in letters:
                dfs(i + 1, currentString + l)
        
        dfs(0, "")

        return res