"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Post-order traversal
        copies = {}
        visited = set()

        if not node:
            return None

        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return copies[node]

            if node not in copies:
                copies[node] = Node(node.val)

            visited.add(node)
            for neighbor in node.neighbors:
                copies[node].neighbors.append(dfs(neighbor))

            return copies[node]

        return dfs(node)