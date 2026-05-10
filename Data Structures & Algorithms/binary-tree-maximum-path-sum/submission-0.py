# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def maxSum(node):
            nonlocal res

            if not node:
                return 0

            left = max(0, maxSum(node.left))
            right = max(0, maxSum(node.right))
            res = max(res, left + right + node.val)

            return node.val + max(left, right)

        maxSum(root)
        return res

        
        