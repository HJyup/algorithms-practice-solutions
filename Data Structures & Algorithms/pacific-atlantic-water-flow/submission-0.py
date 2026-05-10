from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # initial values
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific_set, atlantic_set = set(), set()
        pacific_queue, atlantic_queue = deque(), deque()

        # populate queues
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_queue.append((row, col))
                    pacific_set.add((row, col))
                if row == rows - 1 or col == cols - 1:
                    atlantic_queue.append((row, col))
                    atlantic_set.add((row, col))

        def bfs(q, s):
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for direction in directions:
                        dr, dc = direction
                        r, c = row + dr, col + dc
                        if (
                            0 <= r < rows and
                            0 <= c < cols and
                            (r, c) not in s and
                            heights[r][c] >= heights[row][col]
                        ):
                            q.append((r, c))
                            s.add((r, c))

        # use bfs
        bfs(pacific_queue, pacific_set)
        bfs(atlantic_queue, atlantic_set)

        return [list(coord) for coord in pacific_set & atlantic_set]


        