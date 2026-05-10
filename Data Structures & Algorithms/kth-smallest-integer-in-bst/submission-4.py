# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = k
        res = root.val

        def dfs(node):
            nonlocal curr, res
            if not node:
                return

            dfs(node.left)
            curr -= 1
            if curr == 0:
                res = node.val 
                return
            dfs(node.right)
        
        dfs(root)
        return res


        
        