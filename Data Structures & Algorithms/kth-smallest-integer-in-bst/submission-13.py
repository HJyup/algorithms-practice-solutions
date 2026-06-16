# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, ans = 0, -1

        def dfs(node: Optional[TreeNode]):
            nonlocal count, ans

            if not node or ans != -1:
                return

            dfs(node.left)
            count += 1

            if count == k:
                ans = node.val

            dfs(node.right)

        dfs(root)
        return ans