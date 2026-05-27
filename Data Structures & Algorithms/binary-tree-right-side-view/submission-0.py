class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Edge case
        if not root:
            return []

        # Stores rightmost node from each level
        res = []

        # Queue for BFS
        q = collections.deque([root])

        # Process level by level
        while q:

            levelSize = len(q)

            for i in range(levelSize):

                # Remove node from front
                node = q.popleft()

                # Last node in current level
                if i == levelSize - 1:
                    res.append(node.val)

                # Add valid children only
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res