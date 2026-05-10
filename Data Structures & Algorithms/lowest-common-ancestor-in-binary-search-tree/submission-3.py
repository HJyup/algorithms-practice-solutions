# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = min(p, q, key=lambda x: x.val), max(p, q, key=lambda x: x.val)

        def find(node: TreeNode) -> TreeNode:
            if node.val < p.val:
                return find(node.right)
            
            if node.val > q.val:
                return find(node.left)
            
            return node

        return find(root)
        