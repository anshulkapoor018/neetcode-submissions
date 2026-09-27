# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}

        self.preIdx = 0

        def build(l, r):
            if l > r:
                return None
            
            rootVal = preorder[self.preIdx]
            root = TreeNode(rootVal)
            mid = inorderMap[rootVal]
            self.preIdx += 1

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            
            return root
        
        return build(0, len(inorder) - 1)
            