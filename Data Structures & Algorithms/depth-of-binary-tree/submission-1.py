class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Empty subtree has height 0
            if not node:
                return 0

            # Get heights of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Current node contributes one level
            return 1 + max(left, right)

        return dfs(root)