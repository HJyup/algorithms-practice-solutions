# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def inorder(node):
            nonlocal order

            if not node:
                return None

            inorder(node.left)
            order.append(node.val)
            inorder(node.right)

            return None

        inorder(root)
        return order
        