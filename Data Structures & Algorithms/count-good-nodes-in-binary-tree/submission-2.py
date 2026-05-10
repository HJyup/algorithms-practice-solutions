# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node: TreeNode, mx = float('-inf')):
            nonlocal count

            if not node:
                return None

            if node.val >= mx:
                count += 1

            mx = max(mx, node.val)

            dfs(node.left, mx)
            dfs(node.right, mx)

            return None

        dfs(root)
        return count