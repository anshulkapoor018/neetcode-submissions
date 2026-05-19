class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temp[j] > temp[i]:
                    break
                j += 1
                count += 1
            
            count = 0 if j == n else count
            res.append(count)
        
        return res