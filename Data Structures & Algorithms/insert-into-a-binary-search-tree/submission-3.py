# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        curr = root
        parent = None
        while curr:
            if val > curr.val:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left

        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root
