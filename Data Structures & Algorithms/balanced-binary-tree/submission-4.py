# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optiona[TreeNode]) -> int:
            if not node:
                return 0

            left = check(node.left)
            right = check(node.right)

            if abs(right - left) > 1:
                return float('inf')

            return 1 + max(left, right)


        res = check(root)
        return True if res != float('inf') else False