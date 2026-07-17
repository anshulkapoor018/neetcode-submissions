class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToCopy = {None: None}
        curr = head

        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]