"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid) - 1

        def divide(top: int, down: int, left: int, right: int) -> 'Node':
            # top left = (top, (top + down) // 2, left, (left + right) // 2)
            # top right = (top, (top + down) // 2, (left + right) // 2, right)
            # bottom left = ((top + down) // 2, down, left, (left + right) // 2)
            # bottom right = ((top + down) // 2, down, (left + right) // 2, right)
            if top == down and left == right:
                return Node(val=grid[top][left], isLeaf=True)

            mid_y, mid_x = (top + down) // 2, (left + right) // 2
            top_l = divide(top, mid_y, left, mid_x)
            top_r = divide(top, mid_y, mid_x + 1, right)

            btm_l = divide(mid_y + 1, down, left, mid_x)
            btm_r = divide(mid_y + 1, down, mid_x + 1, right)

            if (top_l.isLeaf and top_r.isLeaf and btm_l.isLeaf and btm_r.isLeaf) and (
                top_l.val == top_r.val == btm_l.val == btm_r.val
            ):
                return Node(val=top_l.val, isLeaf=True)
            else:
                return Node(val=True, isLeaf=False, topLeft=top_l, topRight=top_r, bottomLeft=btm_l, bottomRight=btm_r)
                

        return divide(0, n, 0, n)
        