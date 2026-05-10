# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, mx: int) -> None:
            if not node:
                return 0

            count = 1 if node.val >= mx else 0
            mx = max(mx, node.val)

            count += dfs(node.left, mx) + dfs(node.right, mx)
            return count

        return dfs(root, root.val)