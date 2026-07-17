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
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]

        # remove and insert again since it got accessed
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node from linked list
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)

        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]