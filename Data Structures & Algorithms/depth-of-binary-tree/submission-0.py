# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case:
        # Empty tree has depth 0
        if not root:
            return 0

        # Recursively get depth of left subtree
        leftDepth = self.maxDepth(root.left)

        # Recursively get depth of right subtree
        rightDepth = self.maxDepth(root.right)

        # Current depth =
        # 1 (current node) + deeper subtree
        return 1 + max(leftDepth, rightDepth)