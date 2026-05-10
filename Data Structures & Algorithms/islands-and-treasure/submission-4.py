from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 1. Add all treasure cells
        # 2. INF change to depth of the BFS (Itervate only thourgh INFs)
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        INF = 2147483647

        # Add all treasure cells (we want to do Multisource BFS)
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        depth = 0
        while queue:
            n = len(queue)

            for _ in range(n):
                r, c = queue.popleft()
                grid[r][c] = depth

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if not (0 <= row < rows) or not (0 <= col < cols):
                        continue

                    if grid[row][col] != INF or grid[row][col] == -1 or (row, col) in visited:
                        continue

                    visited.add((row, col))
                    queue.append((row, col))

            depth += 1

        return None