class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Monotonic Stack
        res = [0] * len(temperatures)
        st = [] # Stores pair: (temperature, index)
        
        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                # Remove previous colder temperature
                sTemp, sIdx = st.pop()

                # Number of days waited
                res[sIdx] = i - sIdx
            
            st.append((t, i))

        return res
        
        # brute force
        # res = [0] * len(temperatures)
        
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        
        # return res