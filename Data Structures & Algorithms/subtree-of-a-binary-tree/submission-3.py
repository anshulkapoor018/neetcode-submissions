# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        def isSameTree(node1, node2):
            # Both empty means same structure
            if not node1 and not node2:
                return True

            # One empty means structure differs
            if not node1 or not node2:
                return False

            # Values must match
            if node1.val != node2.val:
                return False

            # Both left and right subtrees must match
            left = isSameTree(node1.left, node2.left)
            right = isSameTree(node1.right, node2.right)

            return left and right
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

