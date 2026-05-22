# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Find the leftmost (smallest) node in a BST.
    def minValueNode(self, root):
        current = root

        while current.left:
            current = current.left

        return current

    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:

        # Base case: node not found.
        if not root:
            return None

        # Search in the right subtree.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Search in the left subtree.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Node found.
        else:
            # Case 1: No left child.
            if not root.left:
                return root.right

            # Case 2: No right child.
            if not root.right:
                return root.left

            # Case 3: Two children.
            # Replace with inorder successor
            # (smallest value in right subtree).
            min_node = self.minValueNode(root.right)

            root.val = min_node.val

            # Delete the duplicate successor node.
            root.right = self.deleteNode(root.right, min_node.val)

        return root