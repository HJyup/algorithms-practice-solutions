# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node: Optional[TreeNode], canRob = False) -> int:
            if not node:
                return 0

            if (node, canRob) in memo:
                return memo[(node, canRob)]

            take = 0
            if not canRob:
                take = node.val + dfs(node.left, True) + dfs(node.right, True)

            skip = dfs(node.left, False) + dfs(node.right, False)

            memo[(node, canRob)] = max(skip, take)
            return memo[(node, canRob)]

        return dfs(root)
        