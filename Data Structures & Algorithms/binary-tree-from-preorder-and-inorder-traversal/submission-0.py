# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nums_idx = {num: i for i, num in enumerate(inorder)}
        read = 0

        for i, num in enumerate(inorder):
            nums_idx[num] = i

        def construct(left: int, right: int) -> Optional[TreeNode]:
            nonlocal read 
            
            if left > right:
                return None

            node = TreeNode(preorder[read])
            read += 1

            position = nums_idx[node.val]

            node.left = construct(left, position - 1)
            node.right = construct(position + 1, right)

            return node

        return construct(0, len(inorder) - 1)