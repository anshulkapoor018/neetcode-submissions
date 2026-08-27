class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        
        # trick and preProcess
        for word in wordList:
            for j in range(len(word)):
                # convert word into various wild card strings
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        q = deque()
        q.append(beginWord)
        res = 1
        
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node == endWord:
                    return res
                
                for j in range(len(node)):
                    pattern = node[:j] + "*" + node[j+1:]
                    
                    for nword in nei[pattern]:
                        if nword not in visit:
                            visit.add(nword)
                            q.append(nword)
                    nei[pattern] = []
            res += 1
        
        return 0