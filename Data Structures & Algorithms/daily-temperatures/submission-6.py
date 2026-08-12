class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *  len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            while st and st[-1][0] < t:
                sTemp, sIdx = st.pop()
                
                res[sIdx] = i - sIdx
            
            st.append((t, i))
        
        return res