class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        delimiter = "#"

        for i in strs:
            counter = len(i)
            res += str(counter) + delimiter + i

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            wordLen = int(s[i:j]) 
            res.append(s[j + 1 : j + 1 + wordLen])
            i = j + 1 + wordLen
        return res
