# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                succ = root.right
                while succ.left:
                    succ = succ.left

                new_right = self.deleteNode(root.right, succ.val)
                succ.left = root.left
                succ.right = new_right
                return succ
            elif root.left or root.right:
                return root.left if root.left else root.right
            else:
                return None

        return root