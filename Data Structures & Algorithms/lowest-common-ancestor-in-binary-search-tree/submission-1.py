# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val, q_val = min(p.val, q.val), max(p.val, q.val)

        while root:
            if root.val < p_val:
                root = root.right

            elif root.val > q_val:
                root = root.left
                
            else:
                return root

        return -1