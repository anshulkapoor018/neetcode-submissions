# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        # Helper function:
        # Checks if two trees are identical
        def isSameTree(p, q):

            # Both nodes are null
            if not p and not q:
                return True

            # One node is null
            if not p or not q:
                return False

            # Values do not match
            if p.val != q.val:
                return False

            # Compare left and right subtrees
            return (
                isSameTree(p.left, q.left)
                and
                isSameTree(p.right, q.right)
            )

        # Empty subtree is always valid
        if not subRoot:
            return True

        # Main tree ended before finding subtree
        if not root:
            return False

        # If trees match starting from current node
        if isSameTree(root, subRoot):
            return True

        # Otherwise search:
        # 1. Left subtree
        # 2. Right subtree
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )