# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Stores maximum diameter found
        self.diameter = 0

        def dfs(node):

            # Height of empty tree = 0
            if not node:
                return 0

            # Get left subtree height
            leftHeight = dfs(node.left)

            # Get right subtree height
            rightHeight = dfs(node.right)

            # Diameter passing through current node
            # = left height + right height
            self.diameter = max(
                self.diameter,
                leftHeight + rightHeight
            )

            # Return height of current subtree
            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return self.diameter