# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        st, curr = [], root

        while st or curr:
            if curr:
                st.append(curr)
        
            if curr and curr.left:
                curr = curr.left
            else:
                curr = st.pop()
                ans.append(curr.val)
                curr = curr.right

        return ans