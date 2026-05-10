# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        
        count = k
        def dfs(node):
            nonlocal res, count

            if not node or res != -1:
                return None

            dfs(node.left)
            count -= 1

            if count == 0:
                res = node.val

            dfs(node.right)
            return None

        dfs(root)
        return res
        