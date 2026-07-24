class Node:
    """Doubly linked list node storing a cache entry."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}              # maps key -> Node, for O(1) lookup
        self.capacity = capacity
        # Dummy head/tail sentinels bound the list so we never need to
        # special-case empty-list or single-node edge cases.
        # left = LRU side (least recently used, gets evicted first)
        # right = MRU side (most recently used, most recently touched)
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Unlink a node from the list, without touching the cache dict."""
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """Insert a node just before the right sentinel — i.e. mark it as most recently used."""
        prev = self.right.prev
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        # Accessing a key counts as "use" — move it to the MRU end
        # by removing and reinserting at the right side.
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key already exists — drop its old position in the list;
            # we'll reinsert a fresh node at the MRU end below.
            self.remove(self.cache[key])

        # Create (or overwrite) the node and mark it as most recently used.
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Over capacity — evict the least recently used node,
            # which sits right after the left sentinel.
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]