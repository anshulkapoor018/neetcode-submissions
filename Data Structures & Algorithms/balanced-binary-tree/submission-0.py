# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Returns:
        # [isBalanced, height]
        def dfs(node):
            # Empty tree is balanced
            # Height of empty tree = 0
            if not node:
                return [True, 0]

            # Recursively get info from left subtree
            leftBalanced, leftHeight = dfs(node.left)

            # Recursively get info from right subtree
            rightBalanced, rightHeight = dfs(node.right)

            # Current node is balanced if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. Height difference <= 1
            balanced = (
                leftBalanced and
                rightBalanced and
                abs(leftHeight - rightHeight) <= 1
            )

            # Height of current node
            height = 1 + max(leftHeight, rightHeight)

            return [balanced, height]

        # Final answer is balance status of root
        return dfs(root)[0]