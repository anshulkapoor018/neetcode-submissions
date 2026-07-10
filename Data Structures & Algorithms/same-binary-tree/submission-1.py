class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
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
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        return dfs(p, q)