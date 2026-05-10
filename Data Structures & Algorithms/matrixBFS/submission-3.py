class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        queue.append((0, 0))
        visited.add((0, 0))

        def checkGridCondition(r, c):
            return min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r, c) in visited

        length = 0
        while queue:
            q_length = len(queue)
            for i in range(q_length):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if checkGridCondition(new_r, new_c):
                        continue
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
            length += 1

        return -1
                    