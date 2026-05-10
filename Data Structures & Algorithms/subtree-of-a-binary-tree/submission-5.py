# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isTheSame(node, subNode):
            if not node and not subNode:
                return True

            if (not node and subNode) or (node and not subNode):
                return False

            if node.val != subNode.val:
                return False

            return isTheSame(node.left, subNode.left) and isTheSame(node.right, subNode.right)

        def search(node):
            if not node:
                return False

            if isTheSame(node, subRoot):
                return True
                
            return search(node.left) or search(node.right)

        return search(root)   