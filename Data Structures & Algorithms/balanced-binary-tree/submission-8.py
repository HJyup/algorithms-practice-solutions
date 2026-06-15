# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Unbalanced(Exception):
    pass

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balance - diff between left, right <= 1

        # return max between left and right
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            if abs(left - right) > 1:
                raise Unbalanced()

            return 1 + max(left, right)

        try:
            dfs(root)
            return True
        except Unbalanced:
            return False