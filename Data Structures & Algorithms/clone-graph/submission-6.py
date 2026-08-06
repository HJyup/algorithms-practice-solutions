"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mp = {}
        def dfs(node: Optional['Node']) -> Optional['Node']:
            mp[node] = Node(node.val)
            copied = mp[node].neighbors
            
            for nei in node.neighbors:
                if nei in mp:
                    copied.append(mp[nei])
                else:
                    copied.append(dfs(nei))

            return mp[node]

        return dfs(node)