# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                ser.append('N')
                return

            ser.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ser)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        idx = 0

        def dfs():
            nonlocal idx

            curr = arr[idx]
            idx += 1
            
            if curr == 'N':
                return
            
            node = TreeNode(int(curr))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
