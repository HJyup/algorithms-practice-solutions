# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, root.val)]

        while stack:
            node, mx = stack.pop()

            count += 1 if node.val >= mx else 0
            mx = max(mx, node.val)

            if node.left:
                stack.append((node.left, mx))

            if node.right:
                stack.append((node.right, mx))

        return count