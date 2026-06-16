# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        sol = {}

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return 

            sol[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        ans = [0] * (max(sol.keys()) + 1)

        for i in range(len(ans)):
            ans[i] = sol[i]

        return ans