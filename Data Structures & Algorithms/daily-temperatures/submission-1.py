class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        # Result array initialized with 0
        # Default 0 means no warmer temperature found in future
        res = [0] * len(temp)

        # Monotonic decreasing stack
        # Stores pair: (temperature, index)
        stack = []

        for i, t in enumerate(temp):

            # If current temperature is warmer than stack top,
            # we found the next warmer day for previous entries
            while stack and t > stack[-1][0]:

                # Remove previous colder temperature
                sTemp, sIdx = stack.pop()

                # Number of days waited
                res[sIdx] = i - sIdx

            # Push current temperature with its index
            stack.append((t, i))

        return res