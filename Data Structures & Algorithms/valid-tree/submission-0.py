from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(child, parent):
            if child in visited:
                return False

            visited.add(child)
            for neighbor in graph[child]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, child):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n