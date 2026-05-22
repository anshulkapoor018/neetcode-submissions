# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null,
        # trees match at this branch
        if not p and not q:
            return True

        # If one node is null and the other isn't,
        # trees are different
        if not p or not q:
            return False

        # Values must match
        if p.val != q.val:
            return False

        # Recursively compare:
        # 1. Left subtrees
        # 2. Right subtrees
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))