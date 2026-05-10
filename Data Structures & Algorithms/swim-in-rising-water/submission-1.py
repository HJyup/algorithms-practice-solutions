import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        # 1. 1 <= grid.length <= 50 
        # 2. Since we are minimising the cost, we should use Dikstra
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)
        # in worst case we will need to traverse all grid and maintain min-heap therefore: n^2 * 2log(n)

        # Represents weight, position
        heap = [(grid[0][0], (0, 0))]
        seen = set()

        while heap:
            weight, position = heapq.heappop(heap)
            if position in seen:
                continue

            res = max(weight, res)
            if position == (n - 1, n - 1):
                return res

            seen.add(position)
            for dr, dc in directions:
                row, col = dr + position[0], dc + position[1]
                if not (0 <= row < n) or not (0 <= col < n):
                    continue

                if (row, col) in seen:
                    continue

                # We are taking their path as neighbour and trying to minise the cost seen on the grid
                heapq.heappush(heap, (grid[row][col], (row, col)))         

        return res