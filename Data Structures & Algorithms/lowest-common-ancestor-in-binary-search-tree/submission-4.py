# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = min(p, q, key=lambda x: x.val), max(p, q, key=lambda x: x.val)

        current = root

        while current:
            if p.val > current.val:
                current = current.right

            elif q.val < current.val:
                current = current.left

            else:
                return current

        return -1
        