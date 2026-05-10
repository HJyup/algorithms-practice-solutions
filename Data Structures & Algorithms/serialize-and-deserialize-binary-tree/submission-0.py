# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []

        def preorder(node):
            nonlocal tokens

            if not node:
                tokens.append('N')
                return None

            tokens.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

            return None

        preorder(root)
        return '#'.join(tokens)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def get_token(data):
            current = ''

            for char in data:
                if char == '#':
                    yield current
                    current = ''

                else:
                    current += char

            if current:
                yield current

            return None

        tokens = get_token(data)

        def build():
            try:
                token = next(tokens)
                if token == 'N':
                    return None

                node = TreeNode(int(token))
                node.left = build()
                node.right = build()

                return node

            except StopIteration:
                return None

        return build()


