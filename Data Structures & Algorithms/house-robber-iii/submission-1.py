# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, 0

            take_l, skip_l = dfs(node.left)
            take_r, skip_r = dfs(node.right)

            return (node.val + skip_l + skip_r, max(take_l, skip_l) + max(skip_r, take_r))

        return max(dfs(root))
        