# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        in_hash = {}
        for i, num in enumerate(inorder):
            in_hash[num] = i

        def dfs(pre_idx: int, left: int, right: int):
            if pre_idx >= len(preorder) or left > right:
                return None

            node = TreeNode(preorder[pre_idx])
            if left == right:
                return node

            in_idx = in_hash[preorder[pre_idx]]
            node.left = dfs(pre_idx + 1, left, in_idx - 1)
            node.right = dfs(pre_idx + (in_idx - left) + 1, in_idx + 1, right)
            return node

        return dfs(0, 0, len(inorder) - 1)

            