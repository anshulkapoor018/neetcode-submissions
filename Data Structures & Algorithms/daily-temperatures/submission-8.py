class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        st = [] # (idx, temp)

        for i, temp in enumerate(temperatures):
            # if current temp is warmer that st top, we found a warmer day
            while st and temp > st[-1][1]:
                sIdx, sTemp = st.pop()
                res[sIdx] = i - sIdx # number of days we waited
            st.append((i, temp))

        return res
