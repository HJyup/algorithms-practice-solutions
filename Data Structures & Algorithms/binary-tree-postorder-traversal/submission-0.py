# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def postorder(node):
            nonlocal order

            if not node:
                return None

            postorder(node.left)
            postorder(node.right)

            order.append(node.val)
            return None

        postorder(root)
        return order