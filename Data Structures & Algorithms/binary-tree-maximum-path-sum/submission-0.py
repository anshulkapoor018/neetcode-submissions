class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global answer:
        # stores the maximum path sum found anywhere in the tree
        res = [root.val]

        def dfs(root):
            """
            Returns:
                Maximum path sum starting at this node and extending
                upward to its parent.

            Important:
                We can only return ONE branch upward
                (either left OR right), not both.
            """

            # Empty subtree contributes nothing
            if not root:
                return 0

            # Best path extending from left subtree
            leftMax = dfs(root.left)

            # Best path extending from right subtree
            rightMax = dfs(root.right)

            # Ignore negative paths because they only reduce our sum
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Path that SPLITS through current node:
            #
            #      left
            #        \
            #         root
            #        /
            #     right
            #
            # This path cannot be returned upward,
            # but it could be the overall answer.
            currentPath = root.val + leftMax + rightMax

            res[0] = max(res[0], currentPath)

            # Return the best SINGLE branch upward.
            #
            # Parent can only continue through one side:
            #
            #      parent
            #         |
            #       root
            #      /
            #   left
            #
            # OR
            #
            #      parent
            #         |
            #       root
            #          \
            #          right
            #
            return root.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]