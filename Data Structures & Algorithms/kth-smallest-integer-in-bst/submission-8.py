# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        self.counter = 0

        def dfs(node):
            if not node:
                self.counter += 1
                return

            dfs(node.left)
            if self.counter == k:
                self.res = node.val
            dfs(node.right)

        dfs(root)
        return self.res


        
        