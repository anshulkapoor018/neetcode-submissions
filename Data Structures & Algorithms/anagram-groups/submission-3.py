class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        strs.sort()

        for i in strs:
            sortedKey = ''.join(sorted(i))
            if sortedKey not in group:
                group[sortedKey] = [i]
            else:
                group[sortedKey].append(i)
        
        res = []

        for k, v in group.items():
            res.append(v)

        return res
    
    