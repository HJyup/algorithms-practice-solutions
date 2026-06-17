# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = float('-inf')
        def dfs(node: Optional[TreeNode]):
            nonlocal ans

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + node.val + right)

            return max(0, node.val + max(left, right))

        dfs(root)
        return ans