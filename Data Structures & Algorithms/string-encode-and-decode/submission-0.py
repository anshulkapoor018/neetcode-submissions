class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "$" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1  # increment until we find first delimiter
            
            l = int(s[i:j]) 
            res.append(s[j + 1 : j + 1 + l])
            i = j + 1 + l
        
        return res