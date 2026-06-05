class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        # left = LRU side, right = MRU side
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Cut node out of its current position
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert node right before self.right
        # This makes it most recently used
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Recently used, so move to MRU side
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node from linked list
            self.remove(self.cache[key])

        # Create/update node
        self.cache[key] = Node(key, value)

        # Insert as most recently used
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]