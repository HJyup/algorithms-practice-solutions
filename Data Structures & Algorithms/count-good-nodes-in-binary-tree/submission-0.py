# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, mx):
            if not node:
                return

            if node.val >= mx:
                self.res += 1

            new_max = max(node.val, mx)
            dfs(node.left, new_max)
            dfs(node.right, new_max)


        dfs(root, root.val)
        return self.res
        