class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")" : "(", "}" : "{", "]" : "["}
        st = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if len(st) == 0 or st[-1] != mapping[i]:
                    return False
                else:
                    st.pop()
        
        return len(st) == 0