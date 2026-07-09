class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def dfs(i):
            # Successfully segmented the entire string
            if i == len(s):
                return True

            # Reuse previously solved suffix
            if i in memo:
                return memo[i]

            # Try every dictionary word at the current position
            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            # No valid segmentation from this index
            memo[i] = False
            return False

        return dfs(0)