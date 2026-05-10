from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific, atlantic = [], []
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        def mark(values):
            queue = deque(values)
            visited = set(values)

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if not (0 <= row < rows) or not (0 <= col < cols):
                        continue

                    if heights[row][col] < heights[r][c] or (row, col) in visited:
                        continue

                    visited.add((row, col))
                    queue.append((row, col))

            return visited

        return list(mark(pacific) & mark(atlantic))