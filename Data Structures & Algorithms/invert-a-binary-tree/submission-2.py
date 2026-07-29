class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # Empty subtree remains empty
            if not node:
                return None

            # Invert left and right subtrees
            invertedLeft = dfs(node.left)
            invertedRight = dfs(node.right)

            # Swap the inverted subtrees
            node.left = invertedRight
            node.right = invertedLeft

            return node

        return dfs(root)