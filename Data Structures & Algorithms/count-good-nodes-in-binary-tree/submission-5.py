# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def count(node: Optional[TreeNode], mx: int) -> None:
            nonlocal res

            if not node:
                return None

            if node.val >= mx:
                res += 1

            mx = max(mx, node.val)
            count(node.left, mx)
            count(node.right, mx)

            return None

        count(root, root.val)
        return res