# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Stores final level order traversal
        res = []

        # Queue for BFS
        q = collections.deque()

        # Start with root node
        q.append(root)

        # Process level by level
        while q:

            # Number of nodes in current level
            levelSize = len(q)

            # Stores values for current level
            level = []

            for i in range(levelSize):

                # Remove node from front of queue
                node = q.popleft()

                # Ignore null nodes
                if node:

                    # Add current node value
                    level.append(node.val)

                    # Add children to queue
                    q.append(node.left)
                    q.append(node.right)

            # Add non-empty level to result
            if level:
                res.append(level)

        return res