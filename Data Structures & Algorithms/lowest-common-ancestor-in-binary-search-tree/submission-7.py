# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p

        def dfs(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None

            if node.val >= p.val and node.val <= q.val:
                return node 
            elif node.val > q.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)