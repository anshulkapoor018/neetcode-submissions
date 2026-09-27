class TrieNode:
    def __init__(self):
        self.children = {} #char -> TreeNode
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEndOfWord = True

    def _findNode(self, s:str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._findNode(word)
        return node is not None and node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        return self._findNode(prefix) is not None

        
        