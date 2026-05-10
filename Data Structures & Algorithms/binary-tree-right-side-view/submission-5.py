# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            lst = None

            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                lst = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if lst:
                res.append(lst)

        return res