# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def attach(self, node: Optional[TreeNode], parent: Optional[TreeNode], new_node: Optional[TreeNode]):
        if not parent:
            return new_node

        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node

        return parent

    def findParent(self, node: Optional[TreeNode], key: int):
        curr = node
        parent = None

        while curr:
            if curr.val == key:
                break
            elif curr.val < key:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left

        return curr, parent

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node, parent = self.findParent(root, key)
        if not node:
            return root

        if not node.left and not node.right:
            res = self.attach(node, parent, None)

        elif node.left and node.right:
            node_r, nxt_node = node.right, None
            while node_r:
                nxt_node = node_r
                node_r = node_r.left

            node.right = self.deleteNode(node.right, nxt_node.val)
            nxt_node.left = node.left
            nxt_node.right = node.right

            res = self.attach(node, parent, nxt_node)

        else:
            nxt = node.left if node.left else node.right
            res = self.attach(node, parent, nxt)

        return root if parent else res