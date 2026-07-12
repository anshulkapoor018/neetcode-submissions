class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #creating a hash
        for i in nums:
            # if num in hash, return true, lookup in hash in O(1)
            if i in seen:
                return True
            seen.add(i)
        return False