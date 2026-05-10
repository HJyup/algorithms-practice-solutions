# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = min(p.val, q.val), max(p.val, q.val)

        def find(node: TreeNode) -> Node:
            if node.val < p:
                return find(node.right)

            if node.val > q:
                return find(node.left)

            return node

        return find(root)